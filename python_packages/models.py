from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=120, unique=True)
    homepage = models.URLField(blank=True, max_length=300)
    documentation = models.URLField(blank=True, max_length=300)
    affiliate_course = models.URLField(blank=True, max_length=500)
    image = models.ImageField(blank=True, upload_to='package_images')
    description = RichTextUploadingField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Category(models.Model):
    tag = models.CharField(max_length=250, unique=True)
    packages = models.ManyToManyField(Package, blank=True, related_name="categories")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.tag
