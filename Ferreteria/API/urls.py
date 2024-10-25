from django.urls import path, include
from . import vistas
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', vistas.ProductoViewSet)
router.register('categoria', vistas.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
