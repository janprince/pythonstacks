from django.contrib.sitemaps import Sitemap
from .models import Book, Category


class BookSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class BookCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Category.objects.all()
