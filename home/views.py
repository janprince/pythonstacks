from django.shortcuts import render
from blog.models import Post


def index(request):
    mostly_viewed_posts = Post.objects.filter(mostly_viewed=True)
    return render(request, "home/index.html", {"mostly_viewed": mostly_viewed_posts,})


def policy(request):
    return render(request, "home/policy.html", {})


def terms(request):
    return render(request, "home/terms.html", {})


def robots(request):
    return render(request, "home/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "home/ads.txt", content_type="text/plain")
