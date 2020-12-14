from django.contrib.sitemaps import Sitemap
from .models import Book, Category


class BookSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.8

    def items(self):
        return Book.objects.all()


class BookCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Category.objects.all()