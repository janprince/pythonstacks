from django.contrib import admin
from .models import *


# Post
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'pub_date', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('featured',)
    search_fields = ['title', 'content']
    actions = ['feature_posts']

    def feature_posts(self, request, queryset):
        queryset.update(featured=True)


# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'important']
    actions = ['make_key']


    def make_key(self, request, queryset):
        queryset.update(important=True)


# Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'post', 'created_on', 'active']
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'message']


# Registering models
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)