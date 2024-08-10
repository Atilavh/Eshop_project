from django.db import models
from jalali_date import date2jalali, datetime2jalali

from accounts_module.models import User


# Create your models here.

class Article_Category(models.Model):
    parent = models.ForeignKey('Article_Category', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'


class Article_List(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, verbose_name='عنوان در url')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    selected_categories = models.ManyToManyField(Article_Category, verbose_name='دسته بندی ها')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام نویسنده', null=True, blank=True,
                               editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
