from django.contrib import admin
from .models import DetalleVenta, Producto  # Asegúrate de importar también el modelo Producto

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1  # Número de filas adicionales en blanco para agregar detalles

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad', 'subtotal']  # Elimina 'venta' ya que no existe en el modelo
