from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Proveedor,Insumo,ItemPedido,Pedido,RecepcionPedido
from django.db.models import F
from rest_framework.views import APIView
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

    def get_serializer_class(self):
        if self.action == 'create':
            return ItemPedidoSerializer
        return ItemPedidoSerializer

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

class ContadorDeInsumosView(APIView):
    def get(self, request):
        insumos = Insumo.objects.all()
        return Response({'cantidad_insumos': insumos.count()})
    
class InsumosBajoStockAPIView(APIView):
    def get(self, request):
        insumos_bajo_stock = Insumo.objects.filter(stock_actual__lte=F('punto_pedido'))
        serializer = InsumoSerializer(insumos_bajo_stock, many=True)
        return Response(serializer.data)
    