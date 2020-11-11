from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    tag = models.CharField(max_length=250)

    def __str__(self):
        return self.tag


class Package(models.Model):
    name = models.CharField(max_length=120)
    project_name = models.CharField(max_length=200, blank=False)
    category = models.ManyToManyField(Category, related_name='packages')
    image = models.ImageField(blank=True, upload_to='package_images')
    description = RichTextField()
    top_library = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('packages:detail', args=[str(self.name)])


class Resource(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField(unique=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.title