# Generated by Django 4.1.13 on 2024-07-20 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='response',
            field=models.TextField(blank=True, default=django.utils.timezone.now, verbose_name='متن پاسخ تماس با ما'),
            preserve_default=False,
        ),
    ]
