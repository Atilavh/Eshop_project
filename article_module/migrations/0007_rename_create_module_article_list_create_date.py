# Generated by Django 4.1.13 on 2024-08-10 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0006_article_list_create_module_alter_article_list_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article_list',
            old_name='create_module',
            new_name='create_date',
        ),
    ]
