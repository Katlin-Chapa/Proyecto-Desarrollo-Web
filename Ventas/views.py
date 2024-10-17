from rest_framework import generics
from .models import DetalleVenta
from .serializers import DetalleVentaSerializer

# Vista para listar y crear detalles de venta
class DetalleVentaListCreateView(generics.ListCreateAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
