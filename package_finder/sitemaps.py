from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse
from datetime import datetime


class PackageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Package.objects.all()