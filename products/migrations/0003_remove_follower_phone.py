# Generated by Django 5.0.1 on 2024-02-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_productimages_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='phone',
        ),
    ]