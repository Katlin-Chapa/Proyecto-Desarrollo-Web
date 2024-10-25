from .models import Categoria

def enlaces_menu(request):
    enlaces = Categoria.objects.all()
    return dict(enlaces=enlaces)
