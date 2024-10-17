from rest_framework import generics
from .models import Producto, Venta
from .serializers import ProductoSerializer, VentaSerializer

# Vista para listar y crear productos
class ProductoListCreateView(generics.ListCreateAPIView):
    """
    Listar todos los productos o crear un nuevo producto.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para listar y crear ventas
class VentaListCreateView(generics.ListCreateAPIView):
    """
    Listar todas las ventas o crear una nueva venta.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

# Vista para obtener detalles de una venta específica
class VentaDetailView(generics.RetrieveAPIView):
    """
    Obtener los detalles de una venta específica.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    lookup_field = 'pk'  # Establecer 'pk' como el campo de búsqueda
