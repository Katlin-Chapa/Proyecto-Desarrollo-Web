from django.urls import path

from Producto import views

urlpatterns = [
    path('ultimos-productos/', views.UltimosProductosList.as_view()),
    path('productos/buscar/', views.buscar),
    path('productos/<slug:categoria_slug>/<slug:producto_slug>/', views.DetalleProducto.as_view()),
    path('productos/<slug:categoria_slug>/', views.DetalleCategoria.as_view()),
]
