from django.db import models


# Create your models here.

class Contact_us(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    email = models.EmailField(verbose_name="ایمیل")
    full_name = models.CharField(max_length=100, verbose_name='نام کامل', null=True, blank=True)
    message = models.TextField(max_length=200, verbose_name='متن تماس با ما')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', null=True)
    crated_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'


class Profile_Picture(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)

