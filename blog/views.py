from django.shortcuts import render
from .models import *

# global variables
categories = Category.objects.all()
recent_posts = Post.objects.filter(featured=True)[:6]   # 6 recent posts


# Index view
def index(request):
    posts = Post.objects.filter(featured=True)



    context = {
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/index.html', context)


# Detail view
def detail(request, slug):
    post = Post.objects.get(slug=slug)



    context = {
        'post': post,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/detail.html', context)
