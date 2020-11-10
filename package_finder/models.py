from django.db import models


# Create your models here.

class Category(models.Model):
    tag = models.CharField(max_length=250)

    def __str__(self):
        return self.tag


class Package(models.Model):
    name = models.CharField(max_length=120)
    category = models.ManyToManyField(Category, related_name='packages')
    image = models.ImageField(blank=True, upload_to='package_images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('packages:detail', args=[str(self.name)])


class Resource(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.title