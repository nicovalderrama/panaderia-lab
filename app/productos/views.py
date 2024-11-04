from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
from .models import Producto
from .serializer import ProductoSerializer
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(isDeleted = False)
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

class ContadorDeProductos(APIView):
    def get(self, request):
        queryset = Producto.objects.all()
        return Response({'cantidad_productos': queryset.count()})
    

# class ProductoCreateView(CreateAPIView):
#     queryset = Producto.objects.all()
#     serializer_class = ProductoSerializer