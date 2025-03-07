from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    slug = models.SlugField(verbose_name='Nombre sin espacios y en minusculas para url')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoría'  
        verbose_name_plural = 'Categorías' 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Categoría')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    slug = models.SlugField(verbose_name='Nombre sin espacios y en minusculas para url')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Imagen')
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Miniatura')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Agregado el')

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Producto'  
        verbose_name_plural = 'Productos'  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
