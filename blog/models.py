from django.db import models
from django.contrib.auth.models import User


# Author model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


# Category model
class Category(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tag}'


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=99)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment: {self.content[:20]} by {self.name}"

