from django.urls import path
from . import views
from blog import views as blog_views

app_name = 'packages'
urlpatterns = [
    path("", views.index, name='index'),
    path("package/<str:project_name>/", views.details, name='detail'),
    path("about/", blog_views.about, name='about'),
    path("contact/", blog_views.contact, name="contact"),
]
