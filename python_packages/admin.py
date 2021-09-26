from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    filter_horizontal = ("packages",)
    search_fields = ['tag']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'featured']
    search_fields = ['name']


# Register your models here.
admin.site.register(Package, PackageAdmin)
admin.site.register(Category, CategoryAdmin)
