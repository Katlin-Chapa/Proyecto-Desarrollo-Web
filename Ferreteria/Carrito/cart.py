from decimal import Decimal
from django.conf import settings
from shop.models import Producto


class Carrito(object):

    def __init__(self, request):
        """
        Inicializamos el carrito
        """
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            # guardar un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        """
        Agregar producto al carrito o actualizar su cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0,
                                         'precio': str(producto.precio)}
        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        self.guardar()

    def guardar(self):
        # Actualizar sesión carrito
        self.session[settings.CART_SESSION_ID] = self.carrito
        # Marcar la sesión como "modificada" para asegurar que se guarde
        self.session.modified = True

    def eliminar(self, producto):
        """
        Eliminar producto del carrito.
        """
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def __iter__(self):
        """
        Iterar sobre los elementos en el carrito y obtener productos de la base de datos.
        """
        producto_ids = self.carrito.keys()
        # Obtener objetos producto y añadirlos al carrito
        productos = Producto.objects.filter(id__in=producto_ids)
        for producto in productos:
            self.carrito[str(producto.id)]['producto'] = producto

        for item in self.carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
        Contar todos los productos en el carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())

    def obtener_precio_total(self):
        """
        Calcular el costo total de los productos en el carrito.
        """
        return sum(Decimal(item['precio']) * item['cantidad'] for item in
                   self.carrito.values())

    def limpiar(self):
        # eliminar el carrito de la sesión
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
