# Generated by Django 4.1.13 on 2024-07-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_module', '0006_alter_contact_us_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
    ]
