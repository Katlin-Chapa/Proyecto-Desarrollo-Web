from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def productos_list(request):
    productos = Producto.objects.all()  # Trae todos los productos
    return render(request, 'inventario.html', {'productos': productos})