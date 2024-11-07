from django.urls import path
from . import views

urlpatterns = [
    path('', views.VehiculosView.as_view(), name='catalogo_vehiculos'),
    path('add/', views.VehiculoCreateView.as_view(), name='crear_vehiculos'),
]
