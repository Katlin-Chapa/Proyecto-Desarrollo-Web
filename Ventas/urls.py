from django.urls import path
from .views import DetalleVentaListCreateView

urlpatterns = [
    path('detalles-venta/', DetalleVentaListCreateView.as_view(), name='detalle-venta-list-create'),
]
