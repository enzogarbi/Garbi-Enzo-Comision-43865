from django.urls import path
from .views import (pagina_menu_view, ClienteList, ClienteCreate,
    ClienteEditView, ClienteDeleteView, ProveedorList, ProveedorCreate,
    ProveedorEditView, ProveedorDeleteView, PaginaOrdenesCompraView,
    PaginaOrdenesCompraListView, SubirOrdenCompraExitosa, subir_orden_compra,BorrarOrdenCompraView)
from . import views

app_name = 'Melfa' 

urlpatterns = [
    path('menu/', pagina_menu_view, name='menu'),
    path('clientes_list/', ClienteList.as_view(), name='cliente_list'),
    path('cliente_create/', ClienteCreate.as_view(), name='cliente_create'),
    path('editar_cliente/<pk>/', ClienteEditView.as_view(), name='editar_cliente'),
    path('borrar_cliente/<pk>/', ClienteDeleteView.as_view(), name='borrar_cliente'),
    path('proveedores_list/', ProveedorList.as_view(), name='proveedor_list'),
    path('proveedor_create/', ProveedorCreate.as_view(), name='proveedor_create'),
    path('editar_proveedor/<pk>/', ProveedorEditView.as_view(), name='editar_proveedor'),
    path('borrar_proveedor/<pk>/', ProveedorDeleteView.as_view(), name='borrar_proveedor'),
    path('ordenes_compra/', PaginaOrdenesCompraView.as_view(), name='ordenes_compra'),
    path('ordenes_compra_list/', PaginaOrdenesCompraListView.as_view(), name='ordenes_compra_list'),
    path('subir_orden_compra_exitosa/', SubirOrdenCompraExitosa.as_view(), name='subir_orden_compra_exitosa'),
    path('subir_orden_compra/', subir_orden_compra, name='subir_orden_compra'),
    path('acerca_de_mi/', views.about_me_view, name='acerca_de_mi'),
    path('buscar_orden_compra/', views.BuscarOrdenCompraView.as_view(), name='buscar_orden_compra'),
    path('borrar_orden_compra/<int:pk>/', BorrarOrdenCompraView.as_view(), name='borrar_orden_compra'),

]
