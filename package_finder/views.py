from django.shortcuts import render, get_object_or_404
import requests
from .models import *
# import markdown

top_packages = Package.objects.filter(top_library=True)


def index(request):
    context = {
        'categories' : Category.objects.all(),
        'top_libraries': top_packages,
    }

    return render(request, "package_finder/index.html", context)


def pypi_api(project_name):
    """
    This function accesses the PyPI API with the given project_name
    and returns a dictionary of some data from response.
    """
    base_url = "https://pypi.org/pypi"

    r = requests.get(f"{base_url}/{project_name}/json")
    data = r.json()
    info = data['info']


    name = info['name']
    author = info['author']
    version = info['version']
    # description = info['description']
    summary = info['summary']
    project_url = info['project_url']
    try:
        documentation = info['project_urls']['Documentation']
    except:
        documentation = "N/A"
    homepage = info['home_page']

    return {'name' : name,
            'author': author,
            'version' : version,
            # 'description': description,
            'summary' : summary,
            'project_url' : project_url,
            'documentation' : documentation,
            'homepage' : homepage
            }


def details(request, project_name):
    data = pypi_api(project_name)
    context = {
        'name': data['name'],
        'version': data['version'],
        'summary': data['summary'],
        # 'description': markdown.markdown(data['description']),
        'project_url': data['project_url'],
        'documentation': data['documentation'],
        'author': data['author'],
        'homepage': data['homepage'],
        'package': get_object_or_404(Package, project_name=project_name),
        'top_libraries': top_packages,
    }
    return render(request, "package_finder/details.html", context)


def policy(request):
    return render(request, "package_finder/policy.html", {'top_libraries': top_packages})


def terms(request):
    return render(request, "package_finder/terms.html", {'top_libraries': top_packages})


def robots(request):
    return render(request, "package_finder/robots.txt", content_type="text/plain")

def ads(request):
    return render(request, "package_finder/ads.txt", content_type="text/plain")