from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    class Tipo(models.TextChoices):
        LIBRE_DE_GLUTEN = 'Gluten Free' , 'Gluten Free'
        VEGANO = 'Vegan' , 'Vegan'
        CONTIENE_TRIGO = 'With Wheat' , 'With Wheat'
        LIBRE_DE_AZUCAR = 'Sugar Free' , 'Sugar Free'

    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    rendimiento = models.IntegerField()
    tipo = models.CharField(
            max_length=50,
            choices=Tipo.choices,
            default=Tipo.CONTIENE_TRIGO,
    )

    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Rinde: {self.rendimiento} porciones"
    
class Packaging(models.Model):
    class Etiqueta(models.TextChoices):
        LIBRE_DE_GLUTEN = 'Gluten Free' , 'Gluten Free'
        VEGANO = 'Vegan' , 'Vegan'
        CONTIENE_TRIGO = 'With Wheat' , 'With Wheat'
        LIBRE_DE_AZUCAR = 'Sugar Free' , 'Sugar Free'
        SIN_ETIQUETA = 'No Label' , 'No Label'

    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    etiqueta = models.CharField(
            max_length=20,
            choices=Etiqueta.choices,
            default=Etiqueta.SIN_ETIQUETA,
    )


    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.etiqueta}"

#class Producto(models.Model):
#    nombre = models.CharField(max_length=100)
#    disponible = models.BooleanField(default=True)
#    rendimiento = models.IntegerField()
#    tipo = models.TextField(blank=True, null=True)

#    def __str__(self):
#        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} - Rinde: {self.rendimiento} porciones"

class Pedido(models.Model):
    nombre_de_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="usuarios")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="pedidos")
    #packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE, related_name="pedidos")
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.producto.nombre} - {self.fecha}"

