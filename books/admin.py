from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    prepopulated_fields = {'slug': ('tag',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', 'author', 'size']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'feedback', 'active']
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)