from django.db import models
from django.contrib.auth import get_user_model
from usuarios.models import Empleado

User = get_user_model()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock_actual = models.IntegerField()
    punto_pedido = models.IntegerField()
    precio_comprado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    proveedor_frecuente = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('recibido', 'Recibido'),
    ]

    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateField(auto_now_add=True)
    numero_pedido = models.CharField(max_length=50, unique=True)
    observaciones = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.numero_pedido:
            self.numero_pedido = self.generar_numero_pedido()
        super().save(*args, **kwargs)

    def generar_numero_pedido(self):
        ultimo_pedido = Pedido.objects.aggregate(max_id=models.Max("id"))
        nuevo_numero = (ultimo_pedido["max_id"] or 0) + 1
        return f"PED-{str(nuevo_numero).zfill(4)}"

class ItemPedido(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="items")

class RecepcionPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(auto_now_add=True)
    recibido_por = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(null=True, blank=True)
