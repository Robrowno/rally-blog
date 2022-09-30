from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt
from .models import Contact, Comment, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .helpers import send_forget_password_mail
import uuid


@csrf_exempt
def home_page(request):
    Post = models.Post.objects.filter(post_status=1).order_by('-created_on')

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)


@csrf_exempt
def post_detail(request, slug):

    post_view = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post_view)
    name = ""
    if request.method == 'POST':
        name = request.user
        body = request.POST.get('comments')
        post = post_view
        Comment.objects.create(name=name, body=body, post=post)

    context = {
        "post": post_view,
        "comments": comments,
        "Username": name

    }
    return render(request, 'pages/post-detail.html', context)


@csrf_exempt
def contact_page(request):

    """
    This function for the contact page checks to see if a form has been posted
    and if all fields in the form have been inputted correctly, it saves it
    and redirects to provide post-submission message.
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

    return render(request, 'pages/contact.html', {'contact': contact, 'submitted': submitted})


@csrf_exempt
def register(request):
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
                messages.error(request, ("Email or Password is wrong, Try Again!"))
                return redirect('login')
        except Exception as e:
            print(e)
            messages.error(request, ("Server error, Please try Again!"))
            return redirect('login')


@csrf_exempt
@login_required(login_url='login')
def profile_page(request):

    """
    Renders the Profile Page
    """
    return render(request, 'pages/my-profile.html')


@csrf_exempt
@login_required(login_url='login')
def edit_profile(request):
    """
    Renders the Edit Profile Page
    """
    return render(request, 'pages/edit-profile.html')


@csrf_exempt
@login_required(login_url='login')
def logout_func(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def follow_page(request):
    return render(request, 'pages/follow-me.html')


@csrf_exempt
def change_password(request, token):
    context = {}
    try:
        profile_obj = models.Profile.objects.filter(forget_password_token=token).first()
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
