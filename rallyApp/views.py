from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . import models

from .models import Contact, Comment, Post


def home_page(request):
    Post = models.Post.objects.filter(post_status=1).order_by('-created_on')

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)


def post_detail(request, slug):

    post_view = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post_view)
    name=""
    if request.method == 'POST':
        name = request.user
        body = request.POST.get('comments')
        post = post_view
        Comment.objects.create(name=name, body=body, post=post)

    context = {
        "post": post_view,
        "comments": comments,
        "Username":name

    }
    print(context)
    return render(request, 'pages/post-detail.html', context)



def follow_page(request):
    return render(request, 'pages/follow-me.html')


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


def login_page(request):
    return render(request, 'pages/login.html')


def register_page(request):
    return render(request, 'pages/register.html')


def reset_password_page(request):
    return render(request, 'pages/reset-password.html')
