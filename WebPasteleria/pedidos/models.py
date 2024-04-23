from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    class Tipo(models.TextChoices):
        LIBRE_DE_GLUTEN = 'GF' , 'Gluten Free'
        VEGANO = 'VG' , 'Vegan'
        CONTIENE_TRIGO = 'WW' , 'With Wheat'
        LIBRE_DE_AZUCAR = 'SF' , 'Sugar Free'

    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    rendimiento = models.IntegerField()
    tipo = models.CharField(
            max_length=2,
            choices=Tipo.choices,
            default=Tipo.CONTIENE_TRIGO,
    )

    
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} - Rinde: {self.rendimiento} porciones"


class Pedido(models.Model):
    nombre_de_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="usuarios")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="pedidos")
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.producto.nombre} - {self.fecha}"

