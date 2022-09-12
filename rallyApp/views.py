from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import ContactForm


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
    This functio for the contact page checks to see if a form has been posted 
    and if all fields in the form have been inputted correctly, it saves it 
    and redirects to provide post-submission message.
    """

    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'pages/contact.html', {'form': form, 'submitted': submitted})


def loginPage(request):
    return render(request, 'pages/login.html')


def registerPage(request):
    return render(request, 'pages/register.html')


def resetPasswordPage(request):
    return render(request, 'pages/reset-password.html')
