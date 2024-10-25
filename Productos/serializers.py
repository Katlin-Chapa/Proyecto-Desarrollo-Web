from rest_framework import serializers
from .models import Categoria, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["id", "nombre", "get_absolute_url", "descripcion", "precio", "get_imagen", "miniatura"]
