from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vehicles/', include('vehicles.urls')),
    path('api/components/', include('components.urls')),
    path('api/pricing/', include('pricing.urls')),
    path('api/services/', include('services.urls')),
]
