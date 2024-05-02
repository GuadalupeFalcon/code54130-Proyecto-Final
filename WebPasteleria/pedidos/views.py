from django.shortcuts import render , redirect
from .models import Pedido, Producto
from django.http import HttpResponse
from .forms import PedidoSearchForm , ProductoCreateForm , PedidoCreateForm , ProductoSearchForm
from django.contrib.auth.models import User

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
    #    return HttpResponse(f"has pedido buscar las reservas de {nombre_de_usuario}")


def create_view(request, nombre_de_usuario, producto):
    pedido = Pedido.objects.create(nombre_de_usuario=nombre_de_usuario, producto=producto)
    return HttpResponse(f"resultado: {pedido}")

def detail_pedidos_view(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    context_dict = {"pedido": pedido}
    return render (request, "pedidos/detail.html", context_dict)

#def search_with_form_view(request):
#    from  .forms import PedidoSearchForm
#    form = PedidoSearchForm()
#    return render(request, "pedidos/form-search.html", context={"search_form":form})


def search_with_form_view(request):
    if request.method == "GET":
        form = PedidoSearchForm()
        return render(request, "pedidos/form-search.html", context={"search_form": form})
    elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = PedidoSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            user = User.objects.get(username = nombre_de_usuario)
            pedidos_del_usuario = Pedido.objects.filter(nombre_de_usuario=user).all()
            contexto_dict = {"pedidos": pedidos_del_usuario}
            return render(request, "pedidos/list.html", contexto_dict)


#def create_producto_with_form_view(request):
#    contexto = {"create-form": ProductoCreateForm() }
#    return render(request, "pedidos/form-create-producto.html", contexto)


#def create_producto_with_form_view(request):
#    if request.method == "GET":
#        contexto = {"create_form_producto": ProductoCreateForm()}
#        return render(request, "pedidos/form-create-producto.html", contexto)
#    elif request.method == "POST":
#        form = ProductoCreateForm(request.POST)
#        if form.is_valid():
#            nombre = form.cleaned_data["nombre"]
#            disponible = form.cleaned_data["disponible"]
#            rendimiento = form.cleaned_data["rendimiento"]
#            tipo = form.cleaned_data["tipo"]
#            nuevo_producto = Producto(
#                nombre=nombre,
#                disponible=disponible,
#                rendimiento=rendimiento,
#                tipo=tipo,
#            )
#            nuevo_producto.save()
#            return detail_producto_view(request, nuevo_producto.id)

def create_producto_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form_producto": ProductoCreateForm()}
        return render(request, "pedidos/form-create-producto.html", contexto)
    elif request.method == "POST":
        form = ProductoCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            rendimiento = form.cleaned_data["rendimiento"]
            tipo = form.cleaned_data["tipo"]
            nuevo_producto = Producto(
                nombre=nombre,
                disponible=disponible,
                rendimiento=rendimiento,
                tipo=tipo,
            )
            nuevo_producto.save()
            return detail_producto_view(request, nuevo_producto.id)
        else:
            # Handle the case where the form is not valid
            return HttpResponse('Form is not valid. Please check the form and try again.')        

def detail_producto_view(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    contexto_dict = {"producto": producto}
    return render(request, "pedidos/detail-producto.html", contexto_dict)


#CRUD: PRODUCTOS

#LIST
#CREATE
#DETAIL
#UPDATE
#DELETE

# CRUD
from django.http import HttpResponse


def producto_list_view(request):
    todos_los_productos = Producto.objects.all()
    contexto = {"SANTIAGOMOTORIZADO": todos_los_productos}
    return render(request, "pedidos/producto-list.html", contexto)

def create_pedido_with_form_view(request):
    contexto = {"create_pedido_form": PedidoCreateForm()}
    return render(request, "pedidos/form-create-pedido.html", contexto)

def delete_producto_view(request, producto_id):
    producto_a_borrar = Producto.objects.filter(id=producto_id).first()
    producto_a_borrar.delete()
    return redirect("productos-list")

def producto_update_view(request, producto_id):
    producto_a_editar = Producto.objects.filter(id=producto_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": producto_a_editar.nombre,
            "disponible": producto_a_editar.disponible,
            "rendimiento": producto_a_editar.rendimiento,
            "tipo": producto_a_editar.tipo,
        }
        formulario = ProductoCreateForm(initial=valores_iniciales)
        contexto = {"form_producto_update": formulario, "OBJETO": producto_a_editar}
        return render(request, "pedidos/form-producto-update.html", contexto)
    elif request.method == "POST":
        form = ProductoCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            rendimiento = form.cleaned_data["rendimiento"]
            descripcion = form.cleaned_data["tipo"]
            producto_a_editar.nombre = nombre
            producto_a_editar.disponible = disponible
            producto_a_editar.rendimiento = rendimiento
            producto_a_editar.descripcion = descripcion
            producto_a_editar.save()
            return redirect("producto-detail", producto_a_editar.id)
        
def search_producto_view(request):
    if request.method == "GET":
        form = ProductoSearchForm()
        return render(request, "pedidos/form-producto-search.html", context={"search_producto_form": form})
    elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = ProductoSearchForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            producto_buscado = Producto.objects.filter(nombre=nombre).all()
            contexto_dict = {"search_producto_form": producto_buscado}
            return render(request, "pedidos/producto-list.html", contexto_dict)