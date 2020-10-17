from django.contrib.sitemaps import Sitemap
from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority =  0.9

    def items(self):
        return Post.objects.filter(featured=True)

    def lastmod(self, obj):
        return obj.pub_date
