from django.contrib.sitemaps import Sitemap
from .models import Post, Category
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ["blog:index", "python_packages:index", "python_packages:disclaimer"]

    def location(self, obj):
        return reverse(obj)


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority =  0.8

    def items(self):
        return Post.objects.filter(featured=True)

    def lastmod(self, obj):
        return obj.pub_date


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Category.objects.all()

