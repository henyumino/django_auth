from django.contrib import admin
from .models import Blog, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(Blog,BlogAdmin)


# Register your models here.
