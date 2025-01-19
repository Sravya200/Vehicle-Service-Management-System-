from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, RepairViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'repairs', RepairViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
