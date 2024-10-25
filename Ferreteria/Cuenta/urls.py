from django.urls import path
from .views import (
    RegistroView,
    LoginView,
    LogoutView,
    MisPedidosView,
)

urlpatterns = [
    path('registrar/', RegistroView.as_view(), name='registrar'),
    path('iniciar-sesion/', LoginView.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    path('mis-pedidos/', MisPedidosView.as_view(), name='mis_pedidos'),
]
