from django.contrib import admin

from Home.models import SiteSetting


# Register your models here.

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_url')


admin.site.register(SiteSetting, SiteSettingAdmin)
