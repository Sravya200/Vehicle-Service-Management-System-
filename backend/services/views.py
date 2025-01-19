from rest_framework import viewsets
from .models import VehicleService
from .serializers import VehicleServiceSerializer

class VehicleServiceViewSet(viewsets.ModelViewSet):
    queryset = VehicleService.objects.all()
    serializer_class = VehicleServiceSerializer
