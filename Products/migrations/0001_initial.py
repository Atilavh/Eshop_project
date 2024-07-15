# Generated by Django 4.1.13 on 2024-07-14 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.TextField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_deleted', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url', models.CharField(db_index=True, max_length=300, verbose_name='عنوان url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_deleted', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=20, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='Products.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='Products.productcategory', verbose_name='دسته بندی ها'),
        ),
    ]
