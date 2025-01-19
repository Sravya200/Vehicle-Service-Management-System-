from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Repair(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='repairs', on_delete=models.CASCADE)
    issue_description = models.TextField()
    repair_needed = models.BooleanField(default=False)
    repair_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repair for {self.vehicle.vehicle_id} on {self.repair_date}"
