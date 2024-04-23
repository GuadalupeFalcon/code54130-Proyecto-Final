from django import forms

from .models import Pedido, Producto


class PedidoSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de usuario"
    )

