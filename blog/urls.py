from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("search/", views.search, name='search'), # must be before detail path
    path("blog/", views.index, name='index'),
    path("blog/<slug:slug>/", views.detail, name="detail"),
    path("category/<str:category_tag>", views.category, name='category'),

]

"""
Note:
    if the search path comes after thr detail path, 'search/' would be taken as a slug 
    and will result in 404 error
"""