from django.contrib.sitemaps import Sitemap
from .models import Package
from django.urls import reverse


class PackageSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Package.objects.filter(featured=True)

    def lastmod(self, obj):
        return obj.pub_date