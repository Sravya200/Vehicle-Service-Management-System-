from rest_framework import serializers
from .models import VehicleService
from vehicles.serializers import VehicleSerializer
from pricing.serializers import ServiceSerializer

class VehicleServiceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    service = ServiceSerializer()

    class Meta:
        model = VehicleService
        fields = '__all__'
