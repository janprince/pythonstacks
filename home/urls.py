from django.urls import path
from . import views
from blog import views as blog_views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("robots.txt", views.robots, name="robots"),
    path("ads.txt", views.ads, name="ads"),
    path("about/", blog_views.about, name='about'),
    path("contact/", blog_views.contact, name="contact"),
    path("privacy-policy/", views.policy, name="policy"),
    path("terms/", views.terms, name="terms"),
]