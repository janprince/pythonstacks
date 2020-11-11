from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project_name', 'top_library']
    prepopulated_fields = {'project_name': ('name',)}
    search_fields = ['name']
    actions = ["make_top_library"]

    def make_top_library(self, request, queryset):
        queryset.update(top_library=True)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'package']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Resource, ResourceAdmin)