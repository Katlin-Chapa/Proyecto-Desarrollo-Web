from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()[:4]
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
