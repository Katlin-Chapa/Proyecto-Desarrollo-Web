from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, ImagenProducto

# Registro del modelo Categoria en el admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Registro del modelo Subcategoria en el admin
@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)

# Registro del modelo Producto en el admin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'subcategoria', 'fecha_ingreso')
    search_fields = ('nombre',)
    list_filter = ('subcategoria',)
    ordering = ('-fecha_ingreso',)

# Registro del modelo ImagenProducto en el admin
@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'imagen')
    search_fields = ('producto__nombre',)
