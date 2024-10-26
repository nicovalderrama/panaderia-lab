from django.db import models
from app.productos.models import Producto

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
    total_monto_venta = models.FloatField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class ItemVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
