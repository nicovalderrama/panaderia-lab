from django.shortcuts import render
from .models import ItemVenta, Venta, Cliente
from rest_framework import viewsets, permissions
from .serializer import ItemVentaSerializer, VentaSerializer, ClienteSerializer
# Create your views here.
class ItemVentaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenta.objects.all()
    serializer_class=ItemVentaSerializer
    permission_classes = [permissions.AllowAny]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class=VentaSerializer
    permission_classes = [permissions.AllowAny]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]