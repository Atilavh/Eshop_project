# Generated by Django 4.1.13 on 2024-07-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام کامل')),
                ('message', models.TextField(max_length=200, verbose_name='متن تماس با ما')),
                ('is_read_by_admin', models.BooleanField(verbose_name='خوانده شده توسط ادمین')),
                ('crated_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('response', models.TextField(blank=True, null=True, verbose_name='متن پاسخ تماس با ما')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
