from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('gerente', 'Gerente'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='vendedor')