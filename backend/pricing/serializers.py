from rest_framework import serializers
from .models import Service
from components.serializers import ComponentSerializer

class ServiceSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'
