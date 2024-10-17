from django.urls import path
from .views import VentaListCreateView

urlpatterns = [
    path('ventas/', VentaListCreateView.as_view(), name='venta-list-create'),
]
