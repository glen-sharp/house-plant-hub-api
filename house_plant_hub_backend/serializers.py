from rest_framework import serializers

from house_plant_hub_backend import models
from config import FULL_MOISTURE_LEVEL, NO_MOISTURE_LEVEL


class PlantSerializer(serializers.ModelSerializer):

    moisture_percentage = serializers.SerializerMethodField("get_latest_moisture_percentage")

    class Meta:
        model = models.Plant
        fields = [
            "id",
            "plant_name",
            "room_name",
            "room_location",
            "moisture_percentage"
        ]

    def get_latest_moisture_percentage(self, plant):
        latest_reading = models.MoistureReading.objects.filter(plant_id=plant).order_by("-reading_datetime").first()
        if latest_reading:
            percentage = (NO_MOISTURE_LEVEL - latest_reading.moisture_level) / (NO_MOISTURE_LEVEL - FULL_MOISTURE_LEVEL)
            return round(percentage * 100, 1)
        else:
            return None


class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoistureReading
        fields = "__all__"
