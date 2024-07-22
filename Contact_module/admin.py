from django.contrib import admin
from Contact_module.models import Contact_us


# Register your models here.
class Contact_usAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'full_name', 'message', 'is_read_by_admin']


admin.site.register(Contact_us, Contact_usAdmin)
