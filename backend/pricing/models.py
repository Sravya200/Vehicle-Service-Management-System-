from django.db import models
from components.models import Component

class Service(models.Model):
    name = models.CharField(max_length=100)
    components = models.ManyToManyField(Component, related_name='services')
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
