from django.shortcuts import render
from . import models


def homePage(request):
    Post = models.Post.objects.all()

    context = {
        "Post": Post
    }
    return render(request, 'pages/index.html', context)
