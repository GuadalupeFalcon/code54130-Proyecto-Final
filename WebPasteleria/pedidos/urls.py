from django.urls import path
from .views import (
    home_view,
    list_view,
    search_view,
    create_view,
    detail_view,
    search_with_form_view
)

urlpatterns = [
    path("", home_view),
    path("list/", list_view, name="pedidos-list"),
    path("detail/<pedido_id>", detail_view),
    path("buscar/<nombre_de_usuario>", search_view),
    path("crear/<nombre_de_usuario>/<producto>", create_view),
    path("buscar-con-formulario", search_with_form_view, name="buscar-con-formulario"),
]
