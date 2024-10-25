from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Producto, Categoria, Marca
from .carrito import Carrito
from .forms import CarritoAgregarProductoForm


@require_POST
def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = CarritoAgregarProductoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrito.agregar(producto=producto,
                        cantidad=cd['cantidad'],
                        actualizar_cantidad=cd['actualizar'])
    return redirect('carrito:detalle_carrito')


def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito:detalle_carrito')


def detalle_carrito(request):
    carrito = Carrito(request)
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'carrito/detalle.html', {'carrito': carrito,
                                                    'categorias': categorias,
                                                    'marcas': marcas})
