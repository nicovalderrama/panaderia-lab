"""
URL configuration for panaderia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app.insumos.views import InsumoViewSet,ProveedorViewSet,ItemPedidoViewSet,PedidoViewSet
from app.productos.views import ProductoViewSet
from app.ventas.views import ItemVentaViewSet,VentaViewSet, ClienteViewSet
from usuarios.views import UsuarioViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"insumos",InsumoViewSet)
router.register(r"proveedor",ProveedorViewSet)
router.register(r"item-pedido",ItemPedidoViewSet)
router.register(r"pedido",PedidoViewSet)
router.register(r"productos",ProductoViewSet)
router.register(r"item-venta",ItemVentaViewSet)
router.register(r"venta",VentaViewSet)
router.register(r"cliente",ClienteViewSet)
router.register(r'usuarios',UsuarioViewSet)
# router.register(r"producto/nuevo", ProductoCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/', UsuarioViewSet.as_view({'get': 'list'})),
    path('api/usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve'})),
    path('',include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
