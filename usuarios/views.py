from rest_framework import viewsets
from .serializer import UsuarioSerializer,EmpleadoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser,Empleado

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return CustomUser.objects.filter(id=user_id)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.get_user_from_token(response.data['access'])
        response.data['user_id'] = user.id
        response.data['role'] = user.role
        return response

    def get_user_from_token(self, token):
        from rest_framework_simplejwt.tokens import AccessToken

        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']
        return CustomUser.objects.get(id=user_id)
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer