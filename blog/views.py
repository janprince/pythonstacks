from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import CommentForm


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
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) # all active comments associated with this post
    new_comment = None

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
    context = {
        'cat_name': category_tag,
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/category.html', context)


def search(request):
    query = render.GET.get('q')
    pass

