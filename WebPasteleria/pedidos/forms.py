from django import forms

from .models import Producto , Pedido

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
        # Specifying which fields should appear in the form, including 'sala'
        fields = [
            "nombre_de_usuario",
            "producto",
            "fecha",
            "hora",
            "descripcion",
        ]
        widgets = {
            "fecha": forms.DateInput(
                attrs={"type": "date"}
            ),  # Use HTML5 date picker for the 'fecha' field
            "hora": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use HTML5 time input for 'hora'
            "descripcion": forms.Textarea(
                attrs={"rows": 3}
            ),  # Provide a larger text area for 'descripcion'
        }

    def __init__(self, *args, **kwargs):
        super(PedidoCreateForm, self).__init__(*args, **kwargs)
        # Optionally, you can further customize the 'sala' field here, for example:
        self.fields["producto"].queryset = Producto.objects.filter(
            disponible=True
        )  # Limit choices to available rooms
        self.fields["producto"].label = "Producto"  # Customize the field label
        # Any other field customizations can be done here
