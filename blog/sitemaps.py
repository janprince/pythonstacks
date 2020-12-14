from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ["home:index", "books:index","packages:index", "blog:index", "home:about", ]

    def location(self, obj):
        return reverse(obj)


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Post.objects.filter(featured=True)

    def lastmod(self, obj):
        return obj.pub_date

