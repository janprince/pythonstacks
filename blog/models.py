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
    important = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tag}'


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)      # default=timezone.now - from django.utils import tim...
    categories = models.ManyToManyField(Category, blank=False, related_name='posts')
    featured = models.BooleanField(default=False)

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


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Message: {self.name} - {self.message[:150]}..."
