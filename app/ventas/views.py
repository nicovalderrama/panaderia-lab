from django.shortcuts import render
from .models import ItemVenta, Venta, Cliente
from rest_framework import viewsets, permissions
from .serializer import ItemVentaSerializer, VentaSerializer, ClienteSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from django.db.models import Sum
from rest_framework.response import Response
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

nombres_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
class ContadorDeVentasDelMes(APIView):
    def get(self, request):
        now = timezone.now()
        primer_dia = now.replace(day=1)
        ultimo_dia = now.replace(day=1, month=now.month % 12 + 1) - timezone.timedelta(days=1)
        mes = nombres_meses[now.month]

        total_ventas = Venta.objects.filter(fecha_venta__range=[primer_dia, ultimo_dia]).count()
        total_recaudado = Venta.objects.filter(fecha_venta__range=[primer_dia, ultimo_dia]).aggregate(total_recaudado=Sum('total_monto_venta'))['total_recaudado']

        return Response({
            'mes': mes,
            'total_ventas': total_ventas,
            'total_recaudado': total_recaudado

        }, status=status.HTTP_200_OK)
    
class ProductosMasVendidos(APIView):
    def get(self, request):
        productos_mas_vendidos = (
            ItemVenta.objects
            .values('producto__nombre')
            .annotate(total_cantidad=Sum('cantidad'))
            .order_by('-total_cantidad')[:3]
        )

        if not productos_mas_vendidos:
            return Response({"message": "No se encontraron productos vendidos"}, status=status.HTTP_204_NO_CONTENT)

        return Response(productos_mas_vendidos, status=status.HTTP_200_OK)