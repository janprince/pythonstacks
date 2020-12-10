from django.urls import path
from . import views


app_name = 'packages'
urlpatterns = [
    path("", views.index, name='index'),
    path("package/<str:project_name>/", views.details, name='detail'),
]
