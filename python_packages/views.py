from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from blog.forms import ContactForm


def index(request):
    categories = Category.objects.all()
    packages = Package.objects.all()
    context = {
        "categories": categories,
        "packages": packages,
    }
    return render(request, "python_packages/index.html", context)


# Contact View
def contact(request):
    new_contact = None

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            new_contact = True

    contact_form = ContactForm()
    context = {
        'title': "Contact",
        'contact_form': contact_form,
        'new_contact': new_contact,
    }

    return render(request, 'python_packages/others/contact.html', context)


# About View
def about(request):
    return render(request, 'python_packages/others/about.html')


def policy(request):
    return render(request, "python_packages/others/policy.html", {})


def disclaimer(request):
    return render(request, "python_packages/others/disclaimer.html", {})


def robots(request):
    return render(request, "python_packages/others/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "python_packages/others/ads.txt", content_type="text/plain")
