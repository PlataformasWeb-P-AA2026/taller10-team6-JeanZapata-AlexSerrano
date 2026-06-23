from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_parroquias, name='listar_parroquias'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('editar_parroquia/<int:id>/', views.editar_parroquia, name='editar_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
    path('editar_barrio/<int:id>/', views.editar_barrio, name='editar_barrio'),
]
