from django.contrib import admin

# Register your models here.

from .models import Category, Comment, Post

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)    