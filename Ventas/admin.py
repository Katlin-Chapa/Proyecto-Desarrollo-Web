from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

# Personalización de la visualización del modelo de Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)

# Modelo inline para ver detalles de una venta directamente en la página de Venta
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1  # Número de filas adicionales en blanco para agregar detalles

# Personalización de la visualización del modelo de Venta
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_venta', 'total')
    search_fields = ('usuario__username', 'fecha_venta')
    inlines = [DetalleVentaInline]  # Para mostrar los detalles de la venta en la misma página
    readonly_fields = ('total', 'fecha_venta')  # Para que los campos no sean editables en el admin

# Registro del modelo DetalleVenta (opcional, ya que aparece como inline en Venta)
@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'subtotal')
    search_fields = ('venta__id', 'producto__nombre')
