from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    MARCAS_VEHICULO = [
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota')
    ]
    
    CATEGORIA_VEHICULO = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga')
    ]
    
    marca = models.CharField(max_length=20, blank=False, null=False, choices=MARCAS_VEHICULO, default='Ford')
    modelo = models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria = models.CharField(max_length=50, blank=False, null=False)
    serial_motor = models.CharField(max_length=50, blank=False, null=False)
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIA_VEHICULO, default='Particular')
    precio = models.PositiveSmallIntegerField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=False, null=False, auto_now_add=False, auto_now=True)
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Valor: {self.precio}"
    
    def condicion_precios(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif 10000 < self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'