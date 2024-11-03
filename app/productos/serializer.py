from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id", "nombre","descripcion","precio_lista", "precio_mayorista","cantidad_disponible","categoria", "imagen", "unidad")
        read_only_fields = ["id"]

