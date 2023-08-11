# models.py

from django.db import models
from django.conf import settings


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    numero_cliente = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    insumo = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class OrdenDeCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_orden = models.CharField(max_length=50)
    archivo = models.FileField(upload_to='ordenes_compra/')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} - {self.numero_orden}'
    

