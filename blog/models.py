from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# Author model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


# Category model
class Category(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    title_representation = models.CharField(max_length=250, blank=False)
    meta_description = models.CharField(max_length=155, blank=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tag}'


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=120, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    slug = models.SlugField(unique=True)
    meta_description = models.CharField(max_length=162, blank=True)
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)      # default=timezone.now - from django.utils import tim...
    categories = models.ManyToManyField(Category, blank=False, related_name='posts')
    featured = models.BooleanField(default=False)
    mostly_viewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=[str(self.slug)])


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=99)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment: {self.comment[:20]}... by {self.name}"


# Comment Reply
class ReplyComment(models.Model):
    name = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies", blank=False)
    reply_message = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Reply: {self.reply_message}"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.name} - {self.message[:150]}..."
