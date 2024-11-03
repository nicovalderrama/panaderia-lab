from rest_framework import serializers
from .models import Proveedor,Insumo,ItemPedido,Pedido, RecepcionPedido
from django.db import transaction
from usuarios.serializer import EmpleadoSerializer

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
class ItemPedidoSerializer(serializers.ModelSerializer):
    insumo_id = serializers.IntegerField(write_only=True)
    insumo = InsumoSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = ["id", "insumo_id", "insumo", "cantidad","pedido_id"]
class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha_solicitud', 'numero_pedido', 'observaciones', 'proveedor', 'usuario', 'estado', 'items']
        read_only_fields = ['id', 'numero_pedido', 'fecha_solicitud']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        with transaction.atomic():
            pedido = Pedido.objects.create(**validated_data)

            for item_data in items_data:
                insumo_id = item_data.pop('insumo_id')
                cantidad = item_data['cantidad']
                
                try:
                    insumo = Insumo.objects.get(id=insumo_id)
                except Insumo.DoesNotExist:
                    raise serializers.ValidationError(f"El insumo con id {insumo_id} no existe.")

                ItemPedido.objects.create(pedido=pedido, insumo=insumo, cantidad=cantidad)
                insumo.save()

        return pedido




class RecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "pedido","fecha_recepcion","observaciones","recibido_por")
        read_only_fields = ["id"]

class ItemRecepcionPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionPedido
        fields = ("id", "insumo", "cantidad_recibida","recepcion_pedido")
        read_only_fields = ["id"]
