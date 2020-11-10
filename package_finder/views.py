from django.shortcuts import render
import requests
from .models import *


def index(request):
    context = {
        'categories' : Category.objects.all(),
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
    version = info['version']
    summary = info['summary']
    description = info['description']
    project_url = info['project_url']
    documentation = info['project_urls']['Documentation']
    homepage = info['home_page']

    return {'name' : name,
            'version' : version,
            'summary' : summary,
            'description' : description,
            'project_url' : project_url,
            'documentation' : documentation,
            'homepage' : homepage
            }


def details(request, package_name):
    data = pypi_api(package_name)
    context = {
        'name': data['name'],
        'version': data['version'],
        'summary': data['summary'],
        'description': data['description'],
        'project_url': data['project_url'],
        'documentation': data['documentation'],
        'homepage': data['homepage'],
        'package': Package.objects.get(name=package_name),
    }
    return render(request, "package_finder/details.html", context)