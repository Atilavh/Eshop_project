from django.contrib import admin
from django.http import HttpResponse
from article_module.models import Article_Category, Article_List


# Register your models here.

class Article_Admin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'parent']
    list_editable = ['url_title', 'is_active', 'parent']


class Article_List_Admin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpResponse, obj: Article_List, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Article_Category, Article_Admin)
admin.site.register(Article_List, Article_List_Admin)
