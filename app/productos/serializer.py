from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id", "nombre","descripcion","precio","cantidad_disponible","categoria", "imagen")
        read_only_fields = ["id"]

