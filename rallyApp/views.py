from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt
from .models import Contact, Comment, Post, Like
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .helpers import send_forget_password_mail
from django.core.paginator import Paginator
import uuid


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
            # Like.objects.filter(post=post, user=user).reaction = 0
            like = get_object_or_404(Like, post=post, user=user)
            like.delete()

        else:
            post.likes.add(user)
            Like.objects.create(user=user, post=post, reaction=1)

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
        print(e)
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
            print(e)
            messages.error(request, ("Server error, Please try Again!"))
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

        user = request.user
        user.first_name = request.POST.get('edit-fname')
        user.last_name = request.POST.get('edit-lname')
        user.username = request.POST.get('edit-username')
        user.email = request.POST.get('edit-email')

        user.save()

        return redirect('profile')

    return render(request, 'pages/edit-profile.html')

# !!! Delete profile in progress !!!


def delete_profile(request):
    """
    Function for deleting user account.
    """
    username = request.user

    if request.method == 'POST':
        try:
            profile = User.objects.get(username=username)
            # messages.warning(
            #     request, 'Are you sure? This action cannot be undone.'
            #     )
            profile.delete()
        except Exception as e:
            return render(
                request, 'pages/edit-profile.html', {'error': e.message}
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
            print("user_id=> "+str(user_id))
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
        print(e)
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
        print(e)
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
        except:
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
    return redirect('../'+slug+'/')


@csrf_exempt
def manage_posts(request):
    """
    """
    post_list = models.Post.objects.filter(post_status=1).order_by('-created_on')
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
    """

    return render(request, 'pages/add-post.html')


def edit_post(request):

    """
    Function for editing a post from the management page.
    """

    return render(request, 'pages/manage-post.html')


def delete_post(request, id):

    """
    Function for deleting a post from the management page.
    """
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        messages.success(request, 'Post was successfully deleted!')
    else:
        messages.error(request, 'Unable to delete the post at this time. Try again later.')

    return HttpResponseRedirect(reverse('home'))
