# Generated by Django 4.1.13 on 2025-05-19 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house_plant_hub_backend', '0002_plant_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moisturereading',
            name='battery_level',
        ),
    ]
