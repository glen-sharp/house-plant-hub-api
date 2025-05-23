# Generated by Django 4.1.13 on 2025-04-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=32, verbose_name='Plant Name')),
                ('room_name', models.CharField(max_length=32, verbose_name='Room Name')),
                ('room_location', models.CharField(max_length=64, verbose_name='Room Location')),
            ],
            options={
                'verbose_name_plural': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='MoistureReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisture_level', models.IntegerField(verbose_name='Soil Moisture Level')),
                ('reading_datetime', models.DateTimeField(auto_now=True, verbose_name='Moisture Reading DateTime')),
                ('battery_level', models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Sensor Battery Level')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house_plant_hub_backend.plant')),
            ],
            options={
                'verbose_name_plural': 'Moisture Readings',
            },
        ),
    ]
