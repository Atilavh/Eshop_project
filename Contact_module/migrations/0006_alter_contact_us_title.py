# Generated by Django 4.1.13 on 2024-07-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_module', '0005_alter_contact_us_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]
