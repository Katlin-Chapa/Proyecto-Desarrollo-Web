from rest_framework import generics
from .models import Venta
from .serializers import VentaSerializer

class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def perform_create(self, serializer):
        serializer.save()
