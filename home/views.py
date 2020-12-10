from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def policy(request):
    return render(request, "home/policy.html", {})


def terms(request):
    return render(request, "home/terms.html", {})


def robots(request):
    return render(request, "home/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "home/ads.txt", content_type="text/plain")
