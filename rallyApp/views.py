import uuid
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.text import slugify
import cloudinary.uploader
from . import models
from .models import Contact, Comment, Post, Like
from .helpers import send_forget_password_mail
from .forms import AddPostForm, UpdatePostForm


@csrf_exempt
def home_page(request):
    """
    Returns a list of posts sorted by post status (Published only) in order of
    publish date. Paginator limits 6 posts to a page.
    """
    post = models.Post.objects.filter(post_status=1).order_by('-created_on')
    paginator = Paginator(post, 6)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {

        "posts": posts
    }

    return render(request, 'pages/index.html', context)


@csrf_exempt
def post_detail(request, slug):

    """
    Fetches post content from a unique slug.
    Also returns a list of comments by fetching user input in
    the comments form.
    """

    post_view = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post_view)
    comment_counter = comments.count()
    # Increase paginator for production version
    paginator = Paginator(comments, 3)
    comment_page_number = request.GET.get('page')
    comments = paginator.get_page(comment_page_number)

    name = ""

    if request.method == 'POST':
        name = request.user
        body = request.POST.get('comments')
        post = post_view
        Comment.objects.create(name=name, body=body, post=post)

    context = {
        "post": post_view,
        "comments": comments,
        "comment_counter": comment_counter,
        "Username": name

    }
    return render(request, 'pages/post-detail.html', context)


def like_post(request, slug):
    """
    Function for liking a post.
    """
    user = request.user
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(user)
            like = get_object_or_404(Like, post=post, user=user)
            like.delete()

        else:
            post.likes.add(user)
            Like.objects.create(user=user, post=post)

    return redirect('post_detail', slug=slug)


@csrf_exempt
def contact_page(request):
    """
    Function for submitting a contact form and saving to database.
    """
    submitted = False
    if request.method == 'POST':

        contact = Contact()
        contact.first_name = request.POST.get('fname')
        contact.last_name = request.POST.get('lname')
        contact.email_address = request.POST.get('validationDefaultEmail')
        contact.query_type = request.POST.get('select-query')
        contact.textbox = request.POST.get('contact-textbox')
        contact.save()
        return HttpResponseRedirect('/contact?submitted=True')
    else:
        contact = Contact()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request, 'pages/contact.html',
        {'contact': contact, 'submitted': submitted}
    )


@csrf_exempt
def register(request):

    """
    Registration taking username, email and password inputs as arguments.
    If neither exist, return to register page with error message.
    """
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                if User.objects.filter(username=username).first():
                    messages.error(request, 'Username is taken.')
                    return redirect('register')

                if User.objects.filter(email=email).first():
                    messages.error(request, 'Email is taken.')
                    return redirect('register')
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                profile_obj = models.Profile.objects.create(user=user)
                profile_obj.save()
                messages.success(request, 'Account registered! Please Login')
                return redirect('login')
            except Exception as e:
                messages.info(request, e)
                return redirect('register')
    except Exception as e:
        messages.error(request, 'Unable to create an account at this time')
    return render(request, "pages/register.html")


@csrf_exempt
def login_func(request):

    """
    Login function taking username and passwords as arguments.
    If user exists, redirect to homepage.
    Else, Error message and return to Login page.
    """

    if request.method == "GET":
        return render(request, 'pages/login.html')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, 'User not found.')
            return redirect('login')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(
                    request, ("Email or Password is wrong, Try Again!")
                    )
                return redirect('login')
        except Exception as e:
            messages.error(request, ("Server error, Please try Again!" + e))
            return redirect('login')


@csrf_exempt
@login_required(login_url='login')
def profile_page(request):
    """
    Renders the Profile Page.
    Displays user info and counts user likes and comments.
    """
    user = request.user
    likes = Like.objects.filter(user=user)
    comments = Comment.objects.filter(name=user)

    count_total_likes = likes.count()
    count_total_comments = comments.count()

    context = {
        "count_total_likes": count_total_likes,
        "count_total_comments": count_total_comments
    }

    return render(request, 'pages/my-profile.html', context)


@csrf_exempt
@login_required(login_url='login')
def edit_profile(request):
    """
    Renders the Edit Profile Page.
    Takes input data and reassigns to user fields.
    Redirects to profile page.
    """

    if request.method == "POST":

        # Data from the form
        username = request.POST.get('edit-username')
        email = request.POST.get('edit-email')
        user_id = request.POST.get('edit_user_id')
        user = request.user
        id = 0
        exist = False
        if User.objects.filter(email=email).exists():
            id = User.objects.filter(
                email=email).values_list('id', flat=True)[0]
            exist = True
        else:
            id = None
        user_id = int(user_id)
        if User.objects.filter(username=username).exists():
            if user_id == id:
                messages.error(request, 'Please update atleast one field')
                return redirect('edit_profile')

            if not exist:
                if (
                    User.objects.filter(username=username).exists()
                ) and user_id == id:
                    messages.error(request, 'This Username already exists.')
                    return redirect('edit_profile')
            else:
                if (
                    User.objects.filter(username=username).exists()
                ) and user_id != id:
                    messages.error(request, 'This Email already exists.')
                    return redirect('edit_profile')
        if User.objects.filter(email=email).exists() and user_id != id:
            messages.error(request, 'That email is already taken.')
            return redirect('edit_profile')

        user.email = email
        user.save()
        messages.success(request, 'Your profile was successfully updated')
        return redirect('edit_profile')
    return render(request, 'pages/edit-profile.html')


def delete_profile(request):
    """
    Function for deleting user account.
    """
    username = request.user

    if request.method == 'POST':
        try:
            profile = User.objects.get(username=username)
            profile.delete()
        except Exception as e:
            return render(
                request, 'pages/edit-profile.html', {'error': e}
                )

    return redirect('home')


@csrf_exempt
@login_required(login_url='login')
def logout_func(request):
    """
    When a request is made by clicking on logout,
    the user is logged out and redirected to the homepage
    """
    logout(request)
    return redirect('/')


@csrf_exempt
def follow_page(request):
    """
    Renders the follow-me social media page.
    """
    return render(request, 'pages/follow-me.html')


@csrf_exempt
def change_password(request, token):

    """
    Function for changing password. Follows from forget_password
    function.
    """
    context = {}
    try:
        profile_obj = models.Profile.objects.filter(
            forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.error(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
            if new_password != confirm_password:
                messages.error(request, 'both should be equal.')
                return redirect(f'/change-password/{token}/')

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
    except Exception as e:
        messages.error(request, 'Profile Object not found')
    return render(request, 'pages/accounts/password_change.html', context)


@csrf_exempt
def forget_password(request):

    """
    Function for changing password, takes username as an argument,
    moves to next function in helpers.py
    """
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.error(request, 'No user found with this username.')
                return redirect('forget-password')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = models.Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email has been sent.')
            return redirect('forget-password')
    except Exception as e:
        messages.error(request, 'Internal Server Error.')
    return render(request, 'pages/accounts/password_reset.html')


@csrf_exempt
def delete_comment(request, pk):

    """
    Function for removing user comment.
    """

    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        try:
            comment.delete()
            messages.success(
                request, 'You have successfully deleted the comment'
                )
        except Exception:
            messages.warning(request, 'The comment could not be deleted.')

    return redirect('home')


@csrf_exempt
def update_comment(request, pk):

    """
    Function for editing post comments.
    When comment is updated, redirects to same post page.
    """

    slug = request.POST['slug']
    comment_id = request.POST['edit_comment_id']
    comment_body = request.POST[str(comment_id)+'_comment_edit_content']
    comment = get_object_or_404(Comment, pk=pk)
    comment.body = comment_body
    comment.save(force_update=True)
    messages.success(request, 'Comment updated!')
    return redirect('../'+slug+'/')


@csrf_exempt
def manage_posts(request):
    """
    Function returns a list of posts for the manage page.
    """
    post_list = Post.objects.filter(post_status=1).order_by('-created_on')
    paginator = Paginator(post_list, 6)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {

        "posts": posts
    }

    return render(request, 'pages/manage-index.html', context)


def add_post(request):

    """
    Function for adding a post from the management page.
    Adds uploaded image to cloudinary.
    """
    if request.method == "POST":
        author = request.user

        file = request.FILES.get('featured_image', None)

        new_post = AddPostForm(request.POST, request.FILES)
        post_save = new_post.save(commit=False)
        post_save.slug = slugify(request.POST['title'])
        post_save.author = author
        post_save.status = 1

        if not file:
            post_save.featured_image = (
                cloudinary.uploader.upload_resource(file)
                )

        post_save.save()
        messages.success(request, 'Successfully created!')
        return redirect('/' + post_save.slug + '?new-post=true')

    if request.method == "GET":
        context = {
            'form': AddPostForm,
            'message': ''
        }
        return render(request, "pages/add-post.html", context)


def edit_post(request, id):

    """
    Function for editing a post from the management page.
    Slug and Image are updated as well if changed.
    """
    context = {
        "message": ""
    }
    if request.method == "GET":
        existing_post = get_object_or_404(Post, id=id)
        form = UpdatePostForm(instance=existing_post)
        context = {
            'form': form,
            'message': ''
        }
        return render(request, "pages/manage-post.html", context)
    if request.method == "POST":
        existing_post = get_object_or_404(Post, id=id)
        file = request.FILES.get(
            'featured_image',
            'https://deconova.eu/wp-content/uploads'
            '/2016/02/default-placeholder.png'
            )

        form = UpdatePostForm(
            request.POST, request.FILES, instance=existing_post
            )

        if form.is_valid():
            form.instance.slug = slugify(request.POST['title'])

            print(file)
            if not file:
                form.instance.featured_image = (
                    cloudinary.uploader.upload_resource(file)
                    )

            form.save()
            messages.success(request, 'Successfully edited!')
            return HttpResponseRedirect('/' + form.instance.slug)

        else:
            print('Post is invalid.')
            print(form.errors)
            messages.error(request, 'Something went wrong!')
            return HttpResponseRedirect('/')
    return render(request, 'pages/manage-post.html', context)


def delete_post(request, id):

    """
    Function for deleting a post from the management page.
    """
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        messages.success(request, 'Post was successfully deleted!')
        return redirect('home')
    else:
        messages.error(
            request, 'Unable to delete the post at this time. Try again later.'
            )

    return HttpResponseRedirect(reverse('home'))


def handler_404(request, exception):
    """
    Function for rendering 404 Error view.
    HTTP status 404 - Not Found
    """

    return render(request, 'pages/errors/404.html')


def handler_500(request):
    """
    Function for rendering 500 Error view.
    HTTP status 500 - Internal Server Error
    """

    return render(request, 'pages/errors/500.html')


def handler_403(request, exception):
    """
    Function for rendering 403 Error view.
    HTTP status 403 - Forbidden
    """

    return render(request, 'pages/errors/403.html')
