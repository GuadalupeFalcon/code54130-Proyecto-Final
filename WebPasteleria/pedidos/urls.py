from django.urls import path
from .views import (
    home_view,
    list_view,
    search_view,
    create_view,
    detail_pedidos_view,
    search_with_form_view,
    create_producto_with_form_view,
    detail_producto_view,
    producto_list_view,
    create_pedido_with_form_view,
    delete_producto_view,
    producto_update_view,
    search_producto_view,
    #VBC
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

urlpatterns = [
    path("", home_view),
    path("list/", list_view, name="pedidos-list"),
    path("detail/<pedido_id>", detail_pedidos_view),
    path("buscar/<nombre_de_usuario>", search_view),
    path("crear/<nombre_de_usuario>/<producto>", create_view),
    path("buscar-con-formulario/", search_with_form_view, name="buscar-con-formulario"),
    path("crear-pedido-con-formulario/", create_pedido_with_form_view, name="crear-pedido-con-formulario"),
    path("crear-producto-con-formulario/", create_producto_with_form_view, name="crear-producto-con-formulario"),
    path("detail-producto/<producto_id>", detail_producto_view, name="producto-detail"),
    path("producto/list/", producto_list_view, name="productos-list"),
    path("producto/delete/<producto_id>", delete_producto_view, name="producto-delete"),
    path("producto/update/<producto_id>", producto_update_view, name="producto-update"),
    path("producto/buscar/", search_producto_view, name="producto-search"),
       # Vistas basadas en clases "VBC"
    path("vbc/list", ProductoListView.as_view(), name="vbc_producto_list"),
    path("vbc/create/", ProductoCreateView.as_view(), name="vbc_producto_create"),
    path("vbc/<int:pk>/detail", ProductoDetailView.as_view(), name="vbc_producto_detail"),
    path("sala/vbc/<int:pk>/update/", ProductoUpdateView.as_view(), name="vbc_producto_update"),
    path("sala/vbc/<int:pk>/delete/", ProductoDeleteView.as_view(), name="vbc_producto_delete"),
]
