from rest_framework import serializers
from .models import CustomUser,Empleado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'role')

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class EmpleadoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = Empleado
        fields = ('id','nombre','cuit','direccion','telefono','email','fecha_nacimiento','fecha_alta','fecha_baja','usuario')