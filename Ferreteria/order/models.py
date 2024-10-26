from django.contrib.auth.models import User
from django.db import models

from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='Usuario')
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(max_length=100, verbose_name='Correo Electrónico')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    zipcode = models.CharField(max_length=20, verbose_name='Código Postal')
    place = models.CharField(max_length=100, verbose_name='Ciudad')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Monto Pagado')
    stripe_token = models.CharField(max_length=100, verbose_name='Token de Stripe')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Orden'
        verbose_name_plural = 'Órdenes'

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Orden')
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE, verbose_name='Producto')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio')
    quantity = models.IntegerField(default=1, verbose_name='Cantidad')

    class Meta:
        verbose_name = 'Artículo de Orden'
        verbose_name_plural = 'Artículos de Orden'

    def __str__(self):
        return f'Artículo {self.id}'
