from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.conf import settings  # import some variables from settings


# global variables
categories = Category.objects.all()
recent_posts = Post.objects.filter(featured=True)[:6]   # 6 recent posts


# Index view
def index(request):
    posts = Post.objects.filter(featured=True)


    # Pagination
    paginator = Paginator(posts, 13)
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
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) # all active comments associated with this post
    new_comment = None

    # Related Posts
    post_cat = post.categories.all().first()  # only generating related posts via just one of the post's category
    related_posts = post_cat.posts.all().exclude(slug=post.slug)[:5]  # only 4 of related posts, excluding current post


    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # pass in the data received to the CommentForm
        if comment_form.is_valid():
            # Create a comment but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()


    context = {
        'post': post,
        'related_posts': related_posts,
        'categories': categories,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'recent_posts': recent_posts,
        'comments': comments,

    }
    return render(request, 'blog/detail.html', context)


# Category view
def category(request, category_tag):
    cat = Category.objects.get(tag=category_tag)
    posts = cat.posts.all()

    # Pagination
    paginator = Paginator(posts, 13)
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
        'cat_name': category_tag,
        'posts': post_list,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/category.html', context)


# View to handle Search
def search(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        print(query.split())# Todo
        query_list = Post.objects.filter(Q(title__icontains=query), featured=True) # Note: two underscores

        context = {
            'posts': query_list,
            'categories': categories,
            'recent_posts': recent_posts,
            'query_count': len(query_list),
            'q': query,
        }
        return render(request, 'blog/search.html', context)
    else:
        return render(request, "blog/search.html", {
            'categories': categories,
            'recent_posts': recent_posts,
        })


# Contact View
def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Message Sent. ")

    contact_form = ContactForm()
    context = {
        'title': "Contact",
        'categories': categories,
        'recent_posts': recent_posts,
        'contact_form': contact_form,
    }

    return render(request, 'blog/contact.html', context)


# About View
def about(request):
    context = {
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/about.html', context)

