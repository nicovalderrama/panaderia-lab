from django.contrib import admin
from .models import Proveedor, Insumo, Pedido, ItemPedido
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Pedido)
admin.site.register(ItemPedido)

