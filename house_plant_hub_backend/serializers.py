from rest_framework import serializers

from house_plant_hub_backend import models


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plant
        fields = "__all__"


class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoistureReading
        fields = "__all__"
