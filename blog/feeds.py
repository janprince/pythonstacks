from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class PostFeed(Feed):
    title = "Posts from PythonStacks"
    link = "/blog/"
    description = "Top Articles from PythonStacks"

    def items(self):
        return Post.objects.filter(featured=True).order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pub_date

    def item_description(self, item):
        if item.subtitle:
            return item.subtitle
        elif item.meta_description:
            return item.meta_description
        else:
            return ""