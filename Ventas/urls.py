from django.urls import path
from .views import ProductoListCreateView, VentaListCreateView, VentaDetailView

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('ventas/', VentaListCreateView.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='venta-detail'),  # Cambiado id por pk
]
