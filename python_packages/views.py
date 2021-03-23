from django.shortcuts import render
from .models import *


def index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "python_packages/index.html", context)


def detail(request, package_name):
    pass
