from rest_framework import serializers
from .models import Producto, DetalleVenta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'subcategoria']  # Añade los campos que necesites


    def create(self, validated_data):
        producto_data = validated_data.pop('producto')
        producto = Producto.objects.get(id=producto_data['id'])
        cantidad = validated_data['cantidad']
        
        # Calcular el subtotal
        subtotal = producto.precio * cantidad
        
        # Crear el detalle de venta
        detalle_venta = DetalleVenta.objects.create(producto=producto, cantidad=cantidad, subtotal=subtotal, **validated_data)  # Asegúrate de pasar los datos validados
        
        # Actualizar el stock del producto
        producto.stock -= cantidad
        producto.save()

        return detalle_venta
