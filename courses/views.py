from django.shortcuts import render
from package_finder.models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "courses/index.html", context)