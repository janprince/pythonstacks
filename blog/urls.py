from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("<slug:slug>/", views.detail, name="detail"),
    path("category/<str:category_tag>", views.category, name='category')
]