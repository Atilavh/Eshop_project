# Generated by Django 4.1.13 on 2024-08-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='site_url',
            field=models.URLField(verbose_name='دامنه سایت'),
        ),
    ]
