from django.db import models
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2)
    precio_mayorista = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.FloatField()
    unidad = models.CharField(max_length=10)
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.isDeleted = True
        self.save()   
