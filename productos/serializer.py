from rest_framework import serializers
from .models import Producto,ItemVenta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id", "nombre","descripcion","precio","cantidad_disponible","categoria")
        read_only_fields = ["id"]

class ItemVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenta
        fields = ("id", "producto","cantidad","monto_total")
        read_only_fields = ["id"]