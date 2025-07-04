# blog/admin.py
from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_date']
    list_filter = ['status', 'category', 'created_date']
    prepopulated_fields = {'slug': ('title',)}