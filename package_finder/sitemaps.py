from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse
import datetime


class PackageSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Package.objects.all()

    def lastmod(self, obj):
        return '45'