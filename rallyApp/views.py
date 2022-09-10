from django.shortcuts import render
from . import models


def homePage(request):
    Post = models.Post.objects.all()

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)


def followPage(request):
    return render(request, 'pages/follow-me.html')


def contactPage(request):
    return render(request, 'pages/contact.html')


def loginPage(request):
    return render(request, 'pages/login.html')


def registerPage(request):
    return render(request, 'pages/register.html')


def resetPasswordPage(request):
    return render(request, 'pages/reset-password.html')
