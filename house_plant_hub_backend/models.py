from django.db import models


class Plant(models.Model):
    plant_name = models.CharField(verbose_name="Plant Name", max_length=32, null=False)
    room_name = models.CharField(verbose_name="Room Name", max_length=32, null=False)
    room_location = models.CharField(verbose_name="Room Location", max_length=64, null=False)

    DisplayFields = ["plant_name", "room_name", "room_location"]

    class Meta:
        verbose_name_plural = "Plants"


class MoistureReading(models.Model):
    moisture_level = models.IntegerField(verbose_name="Soil Moisture Level", null=False)
    reading_datetime = models.DateTimeField(verbose_name="Moisture Reading DateTime", auto_now=True)
    battery_level = models.DecimalField(verbose_name="Sensor Battery Level", decimal_places=2, max_digits=4, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    DisplayFields = ["moisture_level", "reading_datetime", "battery_level", "plant"]

    class Meta:
        verbose_name_plural = "Moisture Readings"
