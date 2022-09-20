from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . import models

from .models import Contact


def home_page(request):
    Post = models.Post.objects.filter(post_status=1).order_by('-created_on')

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)


def post_detail(request, slug):

    Post = models.Post.objects.all()
    Comment = models.Comment.objects.order_by('-posted_on')
    context = {
        "Post": Post,

    }

    post_view = get_object_or_404(Post, slug=slug)
    context['post_view'] = post_view

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
