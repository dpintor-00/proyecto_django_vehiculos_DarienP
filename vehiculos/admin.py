from django.contrib import admin
from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'modelo']
    list_display = ['marca', 'modelo', 'categoria']
    ordering = ['marca']
    list_filter = ['categoria', 'marca']
    