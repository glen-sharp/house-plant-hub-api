from django.contrib import admin

from house_plant_hub_backend import models

admin.site.register(models.Plant)
admin.site.register(models.MoistureReading)
