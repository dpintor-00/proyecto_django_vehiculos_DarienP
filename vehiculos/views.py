from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django import forms

from .models import Vehiculo
   
    
    
# VISTA PARA CREAR NUEVOS VEHICULOS
# LoginRequiredMixin, PermissionRequiredMixin
class VehiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = "vehiculos/crear_vehiculo.html"
    fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    success_url = reverse_lazy('catalogo_vehiculos')
    permission_required = 'vehiculos.add_vehiculo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene permisos para acceder a la vista.")
            return redirect("catalogo_vehiculos")
        
        else:
            messages.info(self.request, "Para continuar, por favor inicie sesión.")
            return redirect("login")
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['marca'].widget.attrs.update({'class': 'form-control my-2'})
        form.fields['modelo'].widget.attrs.update({'class': 'form-control my-2'})
        form.fields['serial_carroceria'].widget.attrs.update({'class': 'form-control my-2'})
        form.fields['serial_motor'].widget.attrs.update({'class': 'form-control my-2'})
        form.fields['categoria'].widget.attrs.update({'class': 'form-control my-2'})
        form.fields['precio'].widget.attrs.update({'class': 'form-control my-2'})
        return form
    
    
class VehiculosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos.html"
    context_object_name = 'autos'
    permission_required = 'vehiculos.view_vehiculo'
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene permisos para acceder a la vista.")
            return redirect("catalogo_vehiculos")
        
        else:
            messages.info(self.request, "Para continuar, por favor inicie sesión.")
            return redirect("login")