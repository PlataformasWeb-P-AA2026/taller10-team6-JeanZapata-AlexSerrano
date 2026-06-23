"""
URL configuration for proyectociudad project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordenamiento/', include('ordenamiento.urls')),
]