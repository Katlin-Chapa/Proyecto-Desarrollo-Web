from rest_framework import serializers
from .models import DetalleVenta
from Inventario.models import Producto  # Ajusta el import según tu estructura de carpetas
from django.contrib.auth.models import User  # Asegúrate de importar el modelo User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']  # Asegúrate de incluir solo los campos necesarios

class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Cambiamos el nombre a 'usuario'

    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'subtotal', 'usuario']  # Usamos 'usuario' en lugar de 'usuario_id'

    def create(self, validated_data):
        producto_data = validated_data.pop('producto')
        producto = Producto.objects.get(id=producto_data['id'])
        cantidad = validated_data['cantidad']
        
        # Calcular el subtotal
        subtotal = producto.precio * cantidad
        
        # Crear el detalle de venta
        detalle_venta = DetalleVenta.objects.create(producto=producto, cantidad=cantidad, subtotal=subtotal, **validated_data)
        
        # Actualizar el stock del producto (asumiendo que existe un campo de stock en Producto)
        producto.stock -= cantidad
        producto.save()

        return detalle_venta
