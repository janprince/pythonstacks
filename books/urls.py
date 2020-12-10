from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="=index"),
    path("category/<str:category_slug>", views.category, name="category"),
    path("book/<str:book_id>", views.detail, name="detail"),
]