from django.contrib import admin
from .models import *

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'parroquia', 'num_parques')

@admin.register(Presidente)
class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'profesion', 'barrio')