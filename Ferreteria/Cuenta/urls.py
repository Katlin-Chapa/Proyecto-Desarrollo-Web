from django.urls import path, reverse_lazy
from .views import VistaRegistro, VistaLogin, VistaEdicion, VistaCuenta
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', VistaLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('shop:product_list')), name='logout'),
    path('registration/', VistaRegistro.as_view(), name='registration'),
    path('edit/', VistaEdicion.as_view(), name='edit'),
    path('account/', VistaCuenta.as_view(), name='account'),
]
