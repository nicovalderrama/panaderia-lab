from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Proveedor,Insumo,ItemPedido,Pedido,RecepcionPedido
from .serializer import  *


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InsumoSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        proveedor_id = self.request.query_params.get('proveedor', None)
        if proveedor_id is not None:
            queryset = queryset.filter(proveedor_frecuente_id=proveedor_id)
        return queryset

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemPedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    def perform_create(self, serializer):
        usuario_id = self.request.data.get('usuario')
        pedido = serializer.save(usuario_id=usuario_id)
        return Response({
        'id': pedido.id,
        'numero_pedido': pedido.numero_pedido,
    })

class RecepcionPedidoViewSet(viewsets.ModelViewSet):
    queryset = RecepcionPedido.objects.all()
    serializer_class = RecepcionPedidoSerializer
    permission_classes = [permissions.AllowAny]
