from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleServiceViewSet

router = DefaultRouter()
router.register(r'vehicle-services', VehicleServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
