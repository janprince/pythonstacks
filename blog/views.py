from django.shortcuts import render
from .models import *
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# global variables
categories = Category.objects.all()
recent_posts = Post.objects.filter(featured=True)[:6]   # 6 recent posts


# Index view
def index(request):
    posts = Post.objects.filter(featured=True)


    # Pagination
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        post_list = paginator.page(paginator.num_pages)



    context = {
        'posts': post_list,
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
