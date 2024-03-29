from django.shortcuts import render, get_object_or_404
from .models import *
# from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import *
from django.db.models import Q
from django.conf import settings  # import some variables from settings


# global variables
categories = Category.objects.all()

# Index view
def index(request):
    posts = Post.objects.filter(featured=True)  #.exclude(Q(title__icontains="course")) # exclude online courses

    context = {
        'posts': posts[:20],
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


# Detail view
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) # all active comments associated with this post
    new_comment = None


    # Next and Previous Posts
    popular_posts = Post.objects.filter(popular=True).order_by('id')


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
        'popular_posts': popular_posts[:4],
        'post': post,
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
def search(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        print(query.split())# Todo
        query_list = Post.objects.filter(Q(title__icontains=query), featured=True) # Note: two underscores

        context = {
            'posts': query_list,
            'categories': categories,
            'query_count': len(query_list),
            'q': query,
        }
        return render(request, 'blog/search.html', context)
    else:
        return render(request, "blog/search.html", {
            'categories': categories,
        })
