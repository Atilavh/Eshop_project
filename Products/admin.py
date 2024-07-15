from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title', 'price', 'is_deleted', 'is_active', 'slug']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTags)
