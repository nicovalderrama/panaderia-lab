from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock_actual = models.IntegerField()
    punto_pedido = models.IntegerField()
    proveedor_frecuente = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Pedido(models.Model):
    fecha_solicitud = models.DateField()
    fecha_recepcion = models.DateField(null=True, blank=True)
    numero_pedido = models.CharField(max_length=50)
    observaciones = models.TextField(null=True, blank=True)

class ItemPedido(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

class RecepcionPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField()
    observaciones = models.TextField(null=True, blank=True)

class ItemRecepcionPedido(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_recibida = models.IntegerField()
    recepcion_pedido = models.ForeignKey(RecepcionPedido, on_delete=models.CASCADE)
