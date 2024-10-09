from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    categoria = models.ForeignKey(Categoria, related_name='subcategorias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.IntegerField(null=False)
    subcategoria = models.ForeignKey(Subcategoria, related_name='productos', on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"

