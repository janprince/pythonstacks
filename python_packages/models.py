from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    pip_name = models.CharField(max_length=70, blank=True)
    image = models.ImageField(blank=True, upload_to='package_images')
    title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(max_length=170, blank=True)
    description = RichTextUploadingField(blank=True)
    meta_data = RichTextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
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
