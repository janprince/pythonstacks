from django.urls import path
from . import views
from blog import views as blog_views

app_name = 'packages'
urlpatterns = [
    path("", views.index, name='index'),
    path("package/<str:project_name>/", views.details, name='detail'),
    path("about/", blog_views.about, name='about'),
    path("contact/", blog_views.contact, name="contact"),
    path("privacy-policy/", views.policy, name="policy"),
    path("terms/", views.terms, name="terms"),
    path("robots.txt", views.robots, name="robots"),
    path("ads.txt", views.ads, name="ads"),
]
