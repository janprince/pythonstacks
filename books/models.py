from django.db import models


class Category(models.Model):
    tag = models.CharField(max_length=120, blank=False, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.tag


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=90)
    categories = models.ManyToManyField(Category, related_name="books", blank=False)
    overview = models.TextField()
    image = models.ImageField(upload_to="book_images")
    download_link = models.URLField(unique=True)
    year = models.IntegerField(blank=False)
    size = models.FloatField(blank=True)
    popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('books:detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    feedback = models.TextField()
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Review by {self.name}"