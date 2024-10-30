from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('gerente', 'Gerente'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='vendedor')


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    cuit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    fecha_nacimiento = models.DateField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to=Q(empleado__isnull=True)
    )