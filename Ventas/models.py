from django.conf import settings
from django.db import models
from Inventario.models import Producto  # Asegúrate de importar el modelo correcto

class Venta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta #{self.id} - {self.fecha_venta}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio * self.cantidad  # Calcular subtotal
        super().save(*args, **kwargs)  # Llama al método save de la clase base

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'
