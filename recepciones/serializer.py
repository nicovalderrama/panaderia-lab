from rest_framework import serializers
from .models import RecepcionPedido,ItemRecepcionPedido

class RecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "pedido","fecha_recepcion","observaciones")
        read_only_fields = "id"

class ItemRecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "insumo", "cantidad_recibida","recepcion_pedido")
        read_only_fields = "id"
