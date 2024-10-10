from django.db import models
from insumos.models import Pedido, Insumo

# Create your models here.
class RecepcionPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField()
    observaciones = models.TextField(null=True, blank=True)

class ItemRecepcionPedido(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_recibida = models.IntegerField()
    recepcion_pedido = models.ForeignKey(RecepcionPedido, on_delete=models.CASCADE)