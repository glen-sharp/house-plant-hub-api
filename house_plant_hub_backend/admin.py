from django.contrib import admin

from house_plant_hub_backend import models


@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = models.Plant.DisplayFields


@admin.register(models.MoistureReading)
class MoistureReadingAdmin(admin.ModelAdmin):
    list_display = models.MoistureReading.DisplayFields

    search_fields = ["plant__plant_name"]
