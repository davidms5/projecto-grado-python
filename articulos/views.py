from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Tickets
from .articulosSerializers import ArticuloSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer
# Create your views here.
