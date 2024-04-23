from django.shortcuts import render
from .models import Pedido, Producto
from django.http import HttpResponse
from .forms import PedidoSearchForm

# Create your views here.

def home_view(request):
    return render (request, "pedidos/home.html")


def list_view(request):
    pedidos = Pedido.objects.all()
    contexto_dict = {"pedidos": pedidos}
    return render(request, "pedidos/list.html", contexto_dict)

def search_view(request, nombre_de_usuario):
    pedidos_del_usuario = Pedido.objects.filter(
        nombre_de_usuario=nombre_de_usuario
    ).all()
    contexto_dict = {"pedidos": pedidos_del_usuario}
    return render(request, "pedidos/list.html", contexto_dict)


def create_view(request, nombre_de_usuario, producto):
    pedido = Pedido.objects.create(nombre_de_usuario=nombre_de_usuario, producto=producto)
    return HttpResponse(f"resultado: {pedido}")

def detail_view(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    context_dict = {"pedido": pedido}
    return render (request, "pedidos/detail.html", context_dict)

def search_with_form_view(request):
    from  .forms import PedidoSearchForm
    form = PedidoSearchForm()
    return render(request, "pedidos/form-search.html", context={"search_form":form})

#CRUD: PRODUCTOS

#LIST
#CREATE
#DETAIL
#UPDATE
#DELETE

