from django.urls import path
from . import views

app_name = "python_packages"
urlpatterns = [
    path("", views.index, name="index"),

    path("robots.txt", views.robots, name="robots"),
    path("ads.txt", views.ads, name="ads"),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.policy, name="policy"),
    path("affiliate-disclaimer/", views.disclaimer, name="disclaimer"),
]