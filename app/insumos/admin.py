from django.contrib import admin
from .models import Proveedor, Insumo, Pedido, ItemPedido, RecepcionPedido, ItemRecepcionPedido
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(RecepcionPedido)
admin.site.register(ItemRecepcionPedido)

