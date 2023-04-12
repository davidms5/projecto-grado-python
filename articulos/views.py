from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Articulo
from .articulosSerializers import ArticuloSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
# Create your views here.
