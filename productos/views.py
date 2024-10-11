from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Producto,ItemVenta
from .serializer import ProductoSerializer,ItemVentaSerializer
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

class ItemVentaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenta.objects.all()
    serializer_class=ItemVentaSerializer
    permission_classes = [permissions.AllowAny]
