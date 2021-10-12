from django.urls import path
from . import views
from blog.feeds import PostFeed


app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("category/<slug:category_slug>/", views.category, name='category'),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("search/", views.search, name='search'),
    path("feed/", PostFeed()),
]

"""
Note:
    if the search path comes after thr detail path, 'search/' would be taken as a slug 
    and will result in 404 error
"""