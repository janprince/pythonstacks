from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("blog/<slug:slug>/", views.detail, name="detail"),
    path("search/", views.search, name='search'),
    path("category/<str:category_tag>", views.category, name='category'),

    path("about/", views.about, name='about'),
    path("contact/", views.contact, name="contact"),

]

"""
Note:
    if the search path comes after thr detail path, 'search/' would be taken as a slug 
    and will result in 404 error
"""