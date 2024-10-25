from rest_framework import serializers
from shop.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ('stock', 'creado', 'actualizado')
