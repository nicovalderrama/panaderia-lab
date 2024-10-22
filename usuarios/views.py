from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import UsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer

    # Este método es opcional si solo necesitas la funcionalidad básica
    def get_queryset(self):
        user_id = self.kwargs.get('pk')  # Obtener el ID del usuario de la URL
        return CustomUser.objects.filter(id=user_id)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.get_user_from_token(response.data['access'])
        response.data['user_id'] = user.id  # Agrega el ID del usuario a la respuesta
        response.data['role'] = user.role    # Agrega el rol del usuario a la respuesta
        return response

    def get_user_from_token(self, token):
        # Lógica para obtener el usuario a partir del token
        from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
        from rest_framework_simplejwt.tokens import AccessToken

        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']
        return CustomUser.objects.get(id=user_id)