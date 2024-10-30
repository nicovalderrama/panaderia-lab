from rest_framework import serializers
from .models import Proveedor,Insumo,ItemPedido,Pedido, RecepcionPedido

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ("id","nombre", "telefono","direccion")
        read_only_fields = ["id"]

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ("id", "nombre", "descripcion", "stock_actual", "punto_pedido", "proveedor_frecuente", "precio_comprado")
        read_only_fields = ["id"]

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'fecha_solicitud', 'numero_pedido', 'observaciones', 'proveedor', 'usuario']
        read_only_fields = ['id', 'numero_pedido', 'fecha_solicitud']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ("id","insumo","cantidad","pedido")
        read_only_fields = ["id"]

class RecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "pedido","fecha_recepcion","observaciones")
        read_only_fields = ["id"]

class ItemRecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "insumo", "cantidad_recibida","recepcion_pedido")
        read_only_fields = ["id"]
