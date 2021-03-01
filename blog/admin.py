from django.contrib import admin
from .models import *


# Post
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('featured', )
    search_fields = ['title', 'overview']
    actions = ['feature_posts']
    filter_horizontal = ("categories",)

    def feature_posts(self, request, queryset):
        queryset.update(featured=True)


# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    prepopulated_fields = {'slug': ('tag',)}


# Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'post', 'created_on', 'active']
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'reply_message', 'comment']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'message']


# Registering models
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)