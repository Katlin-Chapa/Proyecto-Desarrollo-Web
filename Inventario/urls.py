from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, productos_list  # Importa la vista productos_list

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)  # Rutas para la API

urlpatterns = [
    # Rutas para la API
    path('api/', include(router.urls)),

    # Ruta para la vista normal de Django (HTML)
    path('', productos_list, name='inventario'),  # Cambiar a '' para evitar conflicto
]
