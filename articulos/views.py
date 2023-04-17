from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Tickets, Empleados
from .articulosSerializers import ArticuloSerializer, EmpleadosSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer

class CreateUser(generics.CreateAPIView):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
