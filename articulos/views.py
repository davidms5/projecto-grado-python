from django.shortcuts import render
from rest_framework import viewsets, generics
from django.views.decorators.csrf import csrf_exempt
from corsheaders.decorators import cors_headers
from .models import Articulo
from .articulosSerializers import ArticuloSerializer

@csrf_exempt
@cors_headers()
class ArticuloList(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

@csrf_exempt
@cors_headers()
class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
# Create your views here.
