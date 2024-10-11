from rest_framework import serializers
from .models import Cliente,Venta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("nombre_completo", "telefono","direccion","tipo_cliente")
        read_only_fields = "id"

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ("id","fecha_venta", "tipo_venta","forma_pago","tipo_comprobante","numero_comprobante","cliente","items")
        read_only_fields = "id"