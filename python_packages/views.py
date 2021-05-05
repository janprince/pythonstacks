from django.shortcuts import render
from .models import *
from django.contrib import messages
from blog.forms import ContactForm


def index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "python_packages/index.html", context)


def detail(request, package_name):
    package = Package.objects.get(name=package_name)

    context = {
        'package': package,
    }
    return render(request, "python_packages/detail.html", context)


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
        'contact_form': contact_form,
    }

    return render(request, 'blog/others/contact.html', context)


# About View
def about(request):
    return render(request, 'blog/others/about.html')


def policy(request):
    return render(request, "blog/others/policy.html", {})


def terms(request):
    return render(request, "blog/others/terms.html", {})


def robots(request):
    return render(request, "blog/others/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "blog/others/ads.txt", content_type="text/plain")
