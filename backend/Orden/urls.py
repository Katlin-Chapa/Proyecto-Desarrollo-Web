from django.urls import path

from Orden import views

urlpatterns = [
    path('pago/', views.checkout),
    path('ordenes/', views.ListaOrdenes.as_view()),  
]
