from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.CharField(max_length=200, verbose_name='دسته بندی')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.TextField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse('Detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}  {self.price}'








