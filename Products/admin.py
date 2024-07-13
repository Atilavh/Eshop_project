from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'price', 'is_active', 'rating', 'short_description']
    list_filter = ['price', 'is_active', 'rating', 'short_description']
    list_editable = ['is_active', 'rating']


admin.site.register(models.Product, ProductAdmin)
