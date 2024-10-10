from django.db import models
from productos.models import ItemVenta

# Create your models here.
class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=50)

class Venta(models.Model):
    fecha_venta = models.DateField()
    tipo_venta = models.CharField(max_length=50)
    forma_pago = models.CharField(max_length=50)
    tipo_comprobante = models.CharField(max_length=50)
    numero_comprobante = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemVenta)