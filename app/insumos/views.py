from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Proveedor,Insumo,ItemPedido,Pedido
from .serializer import ProveedorSerializer,InsumoSerializer,ItemPedidoSerializer,PedidoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InsumoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemPedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer


