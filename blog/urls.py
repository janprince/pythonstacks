from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("search/", views.search, name='search'), # must be before detail path
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("", views.index, name='index'),
    path("<slug:slug>/", views.detail, name="detail"),
    path("category/<str:category_tag>", views.category, name='category'),


]

"""
Note:
    if the search path comes after thr detail path, 'search/' would be taken as a slug 
    and will result in 404 error
"""