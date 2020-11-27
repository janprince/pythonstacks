from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'free_course', 'priority', 'provider']


admin.site.register(Course, CourseAdmin)
