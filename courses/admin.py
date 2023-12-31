from django.contrib import admin
from .models import Category, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'img')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')
    list_filter = ('created',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
