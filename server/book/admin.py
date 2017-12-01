from django.contrib import admin
from .models import WebSite, Category, Article, Chapter

# Register your models here.

admin.site.register(WebSite)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Chapter)
