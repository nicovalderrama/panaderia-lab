from rest_framework import serializers
from .models import Proveedor,Insumo,ItemPedido,Pedido

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ("id","nombre", "telefono","direccion")
        read_only_fields = ["id"]

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ("id","nombre","descripcion","stock_actual","punto_pedido","proovedor_frecuente")
        read_only_fields = ["id"]

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ("id","fecha_solicitud","fecha_recepcion","numero_pedido","observaciones")
        read_only_fields = ["id"]

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ("id","insumo","cantidad","pedido")
        read_only_fields = ["id"]
    