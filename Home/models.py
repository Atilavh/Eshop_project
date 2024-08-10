from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name="نام سایت")
    site_url = models.URLField(max_length=200, verbose_name="دامنه سایت")
    address = models.CharField(max_length=200, verbose_name="ادرس سایت")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="شماره تلفن")
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name="فکس")
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name="ادرس ایمیل")
    copy_rights = models.TextField(verbose_name="متن کپی رایت")
    about_us_text = models.TextField(verbose_name="متن درباره ما")
    is_main_setting = models.BooleanField(default=False, verbose_name="تنظیمات اصلی")

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name
