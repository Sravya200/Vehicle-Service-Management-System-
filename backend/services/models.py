from django.db import models
from vehicles.models import Vehicle
from pricing.models import Service

class VehicleService(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='services', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='vehicle_services', on_delete=models.CASCADE)
    service_date = models.DateTimeField(auto_now_add=True)
    service_status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return f"{self.vehicle} - {self.service.name} on {self.service_date}"
