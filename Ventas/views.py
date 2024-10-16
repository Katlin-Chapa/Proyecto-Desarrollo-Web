from rest_framework import generics
from .models import Producto, Venta
from .serializers import ProductoSerializer, VentaSerializer

# Vista para listar y crear productos
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para listar y crear ventas
class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

# Vista para obtener detalles de una venta específica
class VentaDetailView(generics.RetrieveAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    lookup_field = 'id'
