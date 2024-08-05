from django.contrib import admin

from article_module.models import Article_Category


# Register your models here.

class Article_Admin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'parent']
    list_editable = ['url_title', 'is_active', 'parent']


admin.site.register(Article_Category, Article_Admin)
