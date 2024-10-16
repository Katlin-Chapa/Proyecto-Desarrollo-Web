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
        venta = Venta.objects.create(**validated_data)
        for detalle_data in detalles_data:
            producto_data = detalle_data.pop('producto')
            producto = Producto.objects.get(id=producto_data['id'])
            DetalleVenta.objects.create(venta=venta, producto=producto, **detalle_data)
            # Actualizar el stock del producto
            producto.stock -= detalle_data['cantidad']
            producto.save()
        return venta
