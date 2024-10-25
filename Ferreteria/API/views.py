from shop.models import Categoria, Producto
from api.serializers import CategoriaSerializer, ProductoSerializer
from rest_framework import viewsets


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
