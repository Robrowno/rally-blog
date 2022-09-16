from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

from .models import Contact


def homePage(request):
    Post = models.Post.objects.all()

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)


def followPage(request):
    return render(request, 'pages/follow-me.html')


def contactPage(request):

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


def loginPage(request):
    return render(request, 'pages/login.html')


def registerPage(request):
    return render(request, 'pages/register.html')


def resetPasswordPage(request):
    return render(request, 'pages/reset-password.html')
