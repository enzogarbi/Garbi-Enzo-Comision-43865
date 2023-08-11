from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cliente, Proveedor, OrdenDeCompra
from .forms import ClienteForm, ProveedorForm, OrdenDeCompraForm
from django.views import View
from django.shortcuts import get_object_or_404

# Vista para el menú principal - requiere que el usuario esté autenticado
@login_required
def pagina_menu_view(request):
    return render(request, 'menu.html')


# Vista de la lista de clientes
class ClienteList(ListView):
    model = Cliente
    template_name = "clientes_list.html"
    context_object_name = "clientes"

    def get_queryset(self):
        queryset = super().get_queryset()
        messages.info(self.request, f"Se encontraron {queryset.count()} clientes.")
        return queryset


# Vista para crear un nuevo cliente
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente_form.html"
    success_url = reverse_lazy('Melfa:cliente_list')


# Vista para editar un cliente
class ClienteEditView(UpdateView):
    model = Cliente
    template_name = 'editar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('Melfa:cliente_list')


# Vista para eliminar un cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirma_borrado.html'
    success_url = reverse_lazy('Melfa:cliente_list')


# Vista de la lista de proveedores
class ProveedorList(ListView):
    model = Proveedor
    template_name = "proveedor_list.html"
    context_object_name = "proveedores"

    def get_queryset(self):
        queryset = super().get_queryset()
        messages.info(self.request, f"Se encontraron {queryset.count()} proveedores.")
        return queryset

# Vista para crear un nuevo proveedor
class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedor_form.html"
    success_url = reverse_lazy('Melfa:proveedor_list')


# Vista para editar un proveedor
class ProveedorEditView(UpdateView):
    model = Proveedor
    template_name = 'editar_proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('Melfa:proveedor_list')


# Vista para eliminar un proveedor
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirmar_borrado.html'
    success_url = reverse_lazy('Melfa:proveedor_list')

# Vista para la página de órdenes de compra
class PaginaOrdenesCompraView(View):
    # Método GET para mostrar la página
    def get(self, request):
        form = OrdenDeCompraForm()
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra.html', {'form': form, 'ordenes': ordenes})
    # Método POST para recibir los datos del formulario
    def post(self, request):
        form = OrdenDeCompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de compra subida correctamente.')
            return redirect('Melfa:subir_orden_compra_exitosa')
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra.html', {'form': form, 'ordenes': ordenes})

# Vista para mostrar una lista de órdenes de compra
class PaginaOrdenesCompraListView(View):
    def get(self, request):
        ordenes = OrdenDeCompra.objects.all()
        return render(request, 'ordenes_compra_list.html', {'ordenes': ordenes})


# Vista para la página de subida exitosa de la orden de compra
class SubirOrdenCompraExitosa(View):
    def get(self, request):
        return render(request, 'subir_orden_compra_exitosa.html')


# Vista para subir una orden de compra
def subir_orden_compra(request):
    if request.method == 'POST':
        form = OrdenDeCompraForm(request.POST, request.FILES)
        if form.is_valid():
            orden_de_compra = form.save(commit=False)
            orden_de_compra.usuario = request.user  # Asigna el usuario actual
            orden_de_compra.save()
            messages.success(request, 'Orden de compra subida correctamente.')
            return redirect('Melfa:subir_orden_compra_exitosa')
    else:
        form = OrdenDeCompraForm()
    return render(request, 'subir_orden_compra.html', {'form': form})


# Vista para la página "Acerca de mí"
def about_me_view(request):
    return render(request, 'acerca_de_mi.html')


# Vista para borrar una orden de compra
class BorrarOrdenCompraView(View):
    def get(self, request, pk):
        orden = get_object_or_404(OrdenDeCompra, pk=pk)
        return render(request, 'borrar_orden_compra.html', {'orden': orden})

    def post(self, request, pk):
        orden = get_object_or_404(OrdenDeCompra, pk=pk)
        orden.delete()
        return redirect('Melfa:ordenes_compra_list')

# Vista para buscar una orden de compra
class BuscarOrdenCompraView(View):
    def get(self, request):
        return render(request, 'buscar_orden_compra.html')

    def post(self, request):
        numero_orden = request.POST.get('numero_orden')
        ordenes = OrdenDeCompra.objects.filter(numero_orden__icontains=numero_orden)
        return render(request, 'buscar_orden_compra.html', {'ordenes': ordenes})
