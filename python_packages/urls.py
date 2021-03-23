from django.urls import path
from . import views

app_name = "python_packages"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:package_name>", views.detail, name="detail"),
]