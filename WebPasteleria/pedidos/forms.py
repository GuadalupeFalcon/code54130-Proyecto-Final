from django import forms
from .models import Producto , Pedido
from .models import Avatar

class ProductoSearchForm(forms.Form):
    nombre= forms.CharField(
        max_length=50, required=True, label="Ingresar nombre del producto"
    )

    
class PedidoSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de usuario"
    )

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'disponible', 'rendimiento', 'tipo']
       
        labels = {
            "nombre": "Nombre del Producto",
            "disponible": "Disponible",
            "rendimiento": "Rendimiento",
            "tipo": "Tipo",
        }

class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["nombre_de_usuario", "producto", "fecha", "hora", "descripcion"]
        labels = { "nombre_de_usuario": "Nombre del Usuario",
            "producto": "Nombre del Producto",
            "fecha": "Fecha",
            "hora": "Hora",
            "descripcion": "Descripción",
        }

from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']