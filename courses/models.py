from django.db import models
from package_finder.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=False, upload_to="course_images")
    affiliate_link = models.URLField()
    provider = models.CharField(max_length=120)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], default=0)
    free_course = models.BooleanField(default=False)

    def __str__(self):
        return f"Course: {self.title}"