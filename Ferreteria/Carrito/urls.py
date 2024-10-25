from django.urls import path
from . import vistas

app_name = 'carrito'

urlpatterns = [
    path('', vistas.detalle_carrito, name='detalle_carrito'),
    path('agregar/<str:producto_id>/', vistas.agregar_carrito, name='agregar_carrito'),
    path('eliminar/<str:producto_id>/', vistas.eliminar_carrito, name='eliminar_carrito'),
]
