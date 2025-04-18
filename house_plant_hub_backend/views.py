from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
import logging

from house_plant_hub_backend import serializers, models

logger = logging.getLogger("root")


@api_view(["GET"])
def readings(request: Request) -> Response:
    """
    API view to return plant moisture readings to client
    """
    plants = models.Plant.objects.filter().all()

    serializer = serializers.PlantSerializer(plants, many=True)

    return Response({"plants_array": serializer.data})


@api_view(["POST"])
@permission_classes([HasAPIKey])
def input_reading(request: Request) -> Response:
    """
    API view to ingest moisture data to database
    """
    try:
        plant_id = request.headers["Plant-ID"]
    except KeyError:
        return Response(
            {"message": "Bad Request: Must include 'Plant-ID' in request header"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        moisture_level = request.query_params["moisture_level"]
    except KeyError:
        return Response(
            {"message": "Bad Request: Must include 'moisture_level' in query params"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    data = {
        "moisture_level": moisture_level,
        "plant": plant_id,
    }
    moisture_reading_serializer = serializers.MoistureSerializer(data=data)
    if moisture_reading_serializer.is_valid():
        moisture_reading_serializer.save()
        return Response(
            {"message": "Moisture reading added"},
            status=status.HTTP_200_OK,
        )
    else:
        logger.error(moisture_reading_serializer.errors)
        return Response(
            {"message": "Bad Request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
