from rest_framework import serializers
from .models import Cliente, Venta, ItemVenta, Producto
from django.db import transaction

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("nombre_completo", "telefono", "direccion", "tipo_cliente", "id")

class ItemVentaSerializer(serializers.ModelSerializer):
    producto_id = serializers.IntegerField(write_only=True)
    producto_nombre = serializers.SerializerMethodField(read_only=True)
    producto_categoria = serializers.SerializerMethodField(read_only=True)
    # producto_precio = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ItemVenta
        fields =  fields = ['producto_id', 'producto_nombre', 'producto_categoria', 'cantidad', 'monto_total', 'producto_precio_unidad', 'tipo_precio']

    def get_producto_nombre(self, obj):
        return obj.producto.nombre  

    def get_producto_precio_mayorista(self, obj):
        return obj.producto.precio_mayorista
    def get_producto_precio_lista(self, obj):
        return obj.producto.precio_lista
    def get_producto_categoria(self, obj):
        return obj.producto.categoria

class VentaSerializer(serializers.ModelSerializer):
    items = ItemVentaSerializer(many=True)
    cliente_nombre_completo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'fecha_venta', 'tipo_venta', 'forma_pago', 'tipo_comprobante', 'numero_comprobante', 'cliente', 'cliente_nombre_completo', 'total_monto_venta', 'user_name_venta', 'items']

    def get_cliente_nombre_completo(self, obj):
        return obj.cliente.nombre_completo  
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        with transaction.atomic():
            venta = Venta.objects.create(**validated_data)

            for item_data in items_data:
                producto_id = item_data.pop('producto_id')
                cantidad_vendida = item_data['cantidad']

                try:
                    producto = Producto.objects.get(id=producto_id)
                except Producto.DoesNotExist:
                    raise serializers.ValidationError(f"El producto con id {producto_id} no existe.")

                if producto.cantidad_disponible < cantidad_vendida:
                    raise serializers.ValidationError(f"El producto {producto.nombre} no tiene suficiente stock.")

                ItemVenta.objects.create(venta=venta, producto=producto, **item_data)

                producto.cantidad_disponible -= cantidad_vendida
                producto.save()

        return venta