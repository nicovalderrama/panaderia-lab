from rest_framework import serializers
from .models import Cliente,Venta, ItemVenta
from django.db import transaction

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("nombre_completo", "telefono","direccion","tipo_cliente", "id")
       
class ItemVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenta
        fields = ['producto', 'cantidad', 'monto_total']

class VentaSerializer(serializers.ModelSerializer):
    items = ItemVentaSerializer(many=True, write_only=True)  

    class Meta:
        model = Venta
        fields = ['fecha_venta', 'tipo_venta', 'forma_pago', 'tipo_comprobante', 'numero_comprobante', 'cliente', 'items']
#falta usuario que hizo la venta en venta
    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Extraemos los items del validated_data

        # Transacción para garantizar atomicidad
        with transaction.atomic():
            venta = Venta.objects.create(**validated_data)

            for item_data in items_data:
                producto = item_data['producto']
                cantidad_vendida = item_data['cantidad']

                # Verificar que haya suficiente stock disponible
                if producto.cantidad_disponible < cantidad_vendida:
                    raise serializers.ValidationError(f"El producto {producto.nombre} no tiene suficiente stock.")

                # Crear el ItemVenta asociado
                ItemVenta.objects.create(venta=venta, **item_data)

                # Actualizar el stock del producto
                producto.cantidad_disponible -= cantidad_vendida
                producto.save()

        return venta