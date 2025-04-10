from rest_framework import serializers

from house_plant_hub_backend import models


class PlantSerializer(serializers.ModelSerializer):

    latest_moisture_reading = serializers.SerializerMethodField("get_latest_moisture_reading")

    class Meta:
        model = models.Plant
        fields = [
            "id",
            "plant_name",
            "room_name",
            "room_location",
            "latest_moisture_reading"
        ]

    def get_latest_moisture_reading(self, plant):
        latest_reading = models.MoistureReading.objects.filter(plant_id=plant).order_by("-reading_datetime").first()
        if latest_reading:
            return latest_reading.moisture_level
        else:
            return None


class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoistureReading
        fields = "__all__"
