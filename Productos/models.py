from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)  
    slug = models.SlugField() 

    class Meta:
        ordering = ("nombre",)  

    def __str__(self):
        return self.nombre 

    def get_absolute_url(self):
        return f"/{self.slug}/"

class Producto(models.Model):
    categoria = models.ForeignKey(
        'Categoria',
        related_name='productos',
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=255)
    slug = models.SlugField()
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    miniatura = models.ImageField(upload_to='uploads/', blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_agregado',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f"/{self.categoria.slug}/{self.slug}/"

    def get_imagen(self):
        if self.imagen:
            return f'http://127.0.0.1:8000{self.imagen.url}'
        return ''

    def make_miniatura(self, imagen, size=(300, 200)):
        img = Image.open(imagen)
        img = img.convert('RGB')
        img.thumbnail(size)  

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail_name = f"thumb_{imagen.name.split('/')[-1]}"
        self.miniatura.save(thumbnail_name, ContentFile(thumb_io.getvalue()), save=False)
        return self.miniatura.url if self.miniatura else ''
