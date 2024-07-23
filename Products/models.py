from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url = models.CharField(max_length=300, db_index=True, verbose_name='عنوان url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_deleted = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان برند', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت')
    category = models.ManyToManyField(
        ProductCategory,
        verbose_name='دسته بندی ها',
        related_name='product_categories')
    Brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name='برند')
    short_description = models.TextField(max_length=360, null=True, db_index=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, unique=True, max_length=200,
                            verbose_name='ادرس دهی url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_deleted = models.BooleanField(verbose_name='حذف شده / نشده', default=False)

    def get_absolute_url(self):
        return reverse('products-details', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}  {self.price}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTags(models.Model):
    caption = models.CharField(max_length=20, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'
