from django.shortcuts import render , redirect
from .models import Pedido, Producto , Packaging
from django.http import HttpResponse
from .forms import PedidoSearchForm , ProductoCreateForm , PedidoCreateForm , ProductoSearchForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render (request, "pedidos/home.html")

@login_required
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

def pedido_update_view(request, pedido_id):
    pedido_a_editar = Pedido.objects.filter(id=pedido_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre_de_usuario": pedido_a_editar.nombre_de_usuario,
            "producto": pedido_a_editar.producto,
            "fecha": pedido_a_editar.fecha,
            "hora": pedido_a_editar.hora,
            "descripcion": pedido_a_editar.descripcion,
        }
        formulario = PedidoCreateForm(initial=valores_iniciales)
        contexto = {"form_pedido_update": formulario, "OBJETO": pedido_a_editar}
        return render(request, "pedidos/form-pedido-update.html", contexto)
    elif request.method == "POST":
        form = PedidoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            producto = form.cleaned_data["producto"]
            fecha = form.cleaned_data["fecha"]
            hora = form.cleaned_data["hora"]
            descripcion = form.cleaned_data["descripcion"]
            pedido_a_editar.nombre_de_usuario = nombre_de_usuario
            pedido_a_editar.producto = producto
            pedido_a_editar.fecha = fecha
            pedido_a_editar.hora = hora
            pedido_a_editar.descripcion = descripcion
            pedido_a_editar.save()
            return redirect("pedido-detail", pedido_a_editar.id)
        
def delete_pedido_view(request, pedido_id):
    pedido_a_borrar = Pedido.objects.filter(id=pedido_id).first()
    pedido_a_borrar.delete()
    return redirect("pedidos-list")

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


@login_required
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
    contexto = {"PRODUCTOS": todos_los_productos}
    return render(request, "pedidos/producto-list.html", contexto)

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
            tipo = form.cleaned_data["tipo"]
            producto_a_editar.nombre = nombre
            producto_a_editar.disponible = disponible
            producto_a_editar.rendimiento = rendimiento
            producto_a_editar.tipo = tipo
            producto_a_editar.save()
            return redirect("producto-detail", producto_a_editar.id)
        
def search_producto_view(request):
    if request.method == "GET":
        contexto={"search_producto_form": ProductoSearchForm()}
        return render (request, "pedidos/form-producto-search.html" , contexto)
    elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = ProductoSearchForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            producto = Producto.objects.filter(nombre=nombre).all()
            contexto = {"PRODUCTOS": producto}
            return render(request, "pedidos/producto-list.html", contexto)
        

def create_pedido_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_pedido_form": PedidoCreateForm()}
        return render(request, "pedidos/form-create-pedido.html", contexto)
    elif request.method == "POST":
        form = PedidoCreateForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            producto = form.cleaned_data["producto"]
            fecha = form.cleaned_data["fecha"]
            hora = form.cleaned_data["hora"]
            descripcion = form.cleaned_data["descripcion"]
            # Obtener el usuario correspondiente al nombre de usuario ingresado
#            usuario = User.objects.get(username=nombre_de_usuario)
            # Obtener el producto seleccionado
#            producto = Producto.objects.get(id=producto_id)
            # Crear un nuevo pedido
            nuevo_pedido = Pedido(
                nombre_de_usuario=nombre_de_usuario,
                producto_id=producto.id,
                fecha=fecha,
                hora=hora,
                descripcion=descripcion,
            )
            nuevo_pedido.save()
            return detail_pedidos_view(request, nuevo_pedido.id)
        
#Producto VBC-------------------------------------   

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ProductoListView(ListView):
    model = Producto
    template_name = "pedidos/vbc/producto-list.html"
    context_object_name = "PRODUCTOS"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "pedidos/vbc/detail-producto.html"
    context_object_name = "producto"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "pedidos/vbc/form-create-producto.html"
    fields = ["nombre", "disponible", "rendimiento", "tipo"]
    success_url = reverse_lazy("vbc_producto_list")


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "pedidos/vbc/form-create-producto.html"
    fields = ["nombre", "disponible", "rendimiento", "tipo"]
    context_object_name = "producto"
    success_url = reverse_lazy("vbc_producto_list")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "pedidos/vbc/producto_confirm_delete.html"
    success_url = reverse_lazy("vbc_producto_list")


#Packaging VBC-------------------------------------   

class PackagingListView(ListView):
    model = Packaging
    template_name = "pedidos/vbc/packaging-list.html"
    context_object_name = "PACKAGING"


class PackagingDetailView(DetailView):
    model = Packaging
    template_name = "pedidos/vbc/detail-packaging.html"
    context_object_name = "producto"


class PackagingCreateView(CreateView):
    model = Packaging
    template_name = "pedidos/vbc/form-create-packaging.html"
    fields = ["nombre", "disponible", "descripcion", "etiqueta"]
    success_url = reverse_lazy("vbc_packaging_list")


class PackagingUpdateView(UpdateView):
    model = Packaging
    template_name = "pedidos/vbc/form-create-packaging.html"
    fields = ["nombre", "disponible", "descripcion", "etiqueta"]
    context_object_name = "form"
    success_url = reverse_lazy("vbc_packaging_list")


class PackagingDeleteView(DeleteView):
    model = Packaging
    template_name = "pedidos/vbc/packaging_confirm_delete.html"
    success_url = reverse_lazy("vbc_packaging_list")



#logIn / LogOut ------------------------------------- 




def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "pedidos/login.html", {"form": form})


from django.contrib.auth.forms import UserCreationForm


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "pedidos/crear_usuario.html", {"form": form})


from django.contrib.auth import logout


def user_logout_view(request):
    logout(request)
    return redirect("login")