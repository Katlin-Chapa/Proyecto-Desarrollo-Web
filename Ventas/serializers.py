from rest_framework import serializers
from .models import Producto, Venta, DetalleVenta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'subtotal']

class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['id', 'usuario', 'fecha_venta', 'total', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        
        if not detalles_data:
            raise serializers.ValidationError("Se debe agregar al menos un detalle de venta.")

        venta = Venta.objects.create(**validated_data)

        total = 0  # Inicializar el total

        for detalle_data in detalles_data:
            producto_data = detalle_data.pop('producto')
            producto = Producto.objects.get(id=producto_data['id'])
            cantidad = detalle_data['cantidad']

            # Crear el DetalleVenta, lo que también calculará el subtotal
            detalle_venta = DetalleVenta(venta=venta, producto=producto, cantidad=cantidad)
            detalle_venta.save()  # Esto guarda y calcula el subtotal automáticamente

            total += detalle_venta.subtotal  # Sumar el subtotal al total

            # Actualizar el stock del producto
            producto.stock -= cantidad
            producto.save()

        venta.total = total  # Asignar el total calculado
        venta.save()  # Guardar la venta con el total actualizado

        return venta
