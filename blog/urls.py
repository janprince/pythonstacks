from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("category/<slug:category_slug>/", views.category, name='category'),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("posts/all/", views.all, name='all'),
    path("robots.txt", views.robots, name="robots"),
    path("ads.txt", views.ads, name="ads"),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.policy, name="policy"),
    path("terms/", views.terms, name="terms"),
]

"""
Note:
    if the search path comes after thr detail path, 'search/' would be taken as a slug 
    and will result in 404 error
"""