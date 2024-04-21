from django.shortcuts import render
from .models import Pedido, Producto

# Create your views here.

def home_view(request):
    return render (request, "pedidos/home.html")


def list_view(request):
    pedidos = Pedido.objects.all()
    contexto_dict = {"pedidos": pedidos}
    return render(request, "pedidos/list.html", contexto_dict)
