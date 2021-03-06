from django.shortcuts import render, get_object_or_404
from .models import *
# from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import *
# from django.db.models import Q
from django.contrib import messages
from django.conf import settings  # import some variables from settings


# global variables
categories = Category.objects.all()

# Index view
def index(request):
    posts = Post.objects.filter(featured=True)

    context = {
        'posts': posts[:10],
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


def all(request):
    posts = Post.objects.filter(featured=True).order_by('id')

    context = {
        'all': True,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/all.html', context)


# Detail view
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) # all active comments associated with this post
    new_comment = None


    # Next and Previous Posts
    all_posts = Post.objects.filter(featured=True).order_by('id')
    posts_list = list(all_posts)
    try:
        current_index = posts_list.index(post)
    except:
        current_index = 0
    try:
        next_post = posts_list[current_index + 1]
    except IndexError:
        next_post = posts_list[0]

    try:
        prev_post = posts_list[current_index - 1]
    except IndexError:
        prev_post = posts_list[len(posts_list)-1]

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
        'next_post': next_post,
        'prev_post': prev_post,
        'categories': categories,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'comments': comments,

    }
    return render(request, 'blog/detail.html', context)


# Category view
def category(request, category_slug):
    cat = Category.objects.get(slug=category_slug)
    posts = cat.posts.filter(featured=True)

    context = {
        'category': cat,
        'posts': posts,
        'categories': categories,}
    return render(request, 'blog/category.html', context)


# View to handle Search
# def search(request):
#     if request.GET.get('q'):
#         query = request.GET.get('q')
#         print(query.split())# Todo
#         query_list = Post.objects.filter(Q(title__icontains=query), featured=True) # Note: two underscores
#
#         context = {
#             'posts': query_list,
#             'categories': categories,
#             'recent_posts': recent_posts,
#             'query_count': len(query_list),
#             'q': query,
#         }
#         return render(request, 'blog/search.html', context)
#     else:
#         return render(request, "blog/search.html", {
#             'categories': categories,
#         })


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
        'contact_form': contact_form,
    }

    return render(request, 'blog/others/contact.html', context)


# About View
def about(request):
    context = {
        'categories': categories,
    }
    return render(request, 'blog/others/about.html', context)


def policy(request):
    return render(request, "blog/others/policy.html", {})


def terms(request):
    return render(request, "blog/others/terms.html", {})


def robots(request):
    return render(request, "blog/others/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "blog/others/ads.txt", content_type="text/plain")