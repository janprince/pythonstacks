from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'package']


admin.site.register(Category)
admin.site.register(Package)
admin.site.register(Resource)