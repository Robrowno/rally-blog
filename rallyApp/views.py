from django.shortcuts import render, get_object_or_404, redirect
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
                messages.error(request, 'Not user found with this username.')
                return redirect('forget-password')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = models.Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email is sent.')
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
    pass
    # id = request.POST['edit_comment_id']
    # # pk = request.POST['edit_post_id']
    # comment = get_object_or_404(Comment, pk=pk)
    # edit = False
    # print(comment.body)
    # if request.method == 'POST':
    #     form = EditCommentForm(request.POST)
    #     if form.is_valid():
    #         # comment.body = form.cleaned_data('')
    #         comment.body=request.POST['comments']
    #         comment.save()
    #         messages.error(request, 'Comment updated  sucessfully')
    #         return redirect('home')
    #     else:
    #         form = EditCommentForm()
    #         if 'edit' in request.GET:
    #             edit = True
    #             messages.error(request, 'Failed to update the comment')
    #             return redirect('home')
    #         return render(request, "pages/post-detail.html")
