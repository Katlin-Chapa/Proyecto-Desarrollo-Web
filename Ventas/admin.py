from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1  # Número de filas adicionales en blanco para agregar detalles



@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha_venta', 'total']  # Asegúrate de que estos campos existan en tu modelo
    inlines = [DetalleVentaInline]  # Agregar detalles de venta en la misma página
    search_fields = ['usuario']  # Para buscar ventas por usuario

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'subtotal']  # Asegúrate de que estos campos existan en tu modelo
