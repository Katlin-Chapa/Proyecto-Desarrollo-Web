from rest_framework import serializers

from .models import Categoria, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            "id",
            "nombre",  # Cambiado de 'name' a 'nombre'
            "get_absolute_url",
            "descripcion",  # Cambiado de 'description' a 'descripcion'
            "precio",  # Cambiado de 'price' a 'precio'
            "get_image",
            "get_thumbnail"
        )

class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True)  # Cambiado de 'products' a 'productos'

    class Meta:
        model = Categoria
        fields = (
            "id",
            "nombre",  # Cambiado de 'name' a 'nombre'
            "get_absolute_url",
            "productos",  # Cambiado de 'products' a 'productos'
        )
