from django.urls import path, include
from . import views  

urlpatterns = [
    path('ultimos-productos/', views.LatestProductsList.as_view(), name='ultimos-productos'),
]
