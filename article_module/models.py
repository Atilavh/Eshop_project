from django.db import models


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
