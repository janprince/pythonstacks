from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True, upload_to='package_images')
    description = RichTextUploadingField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('python_packages:detail', args=[str(self.slug)])


class Category(models.Model):
    tag = models.CharField(max_length=250, unique=True)
    packages = models.ManyToManyField(Package, blank=True, related_name="categories")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.tag