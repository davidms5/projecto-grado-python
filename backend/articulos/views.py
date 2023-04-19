import io
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.http import FileResponse
from django.views.decorators.http import require_GET
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Tickets, Empleados
from .articulosSerializers import ArticuloSerializer, EmpleadosSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = ArticuloSerializer

@require_GET
def download_pdf(request, pk):
    obj = Tickets.objects.get(uuid=pk)
    serializer = ArticuloSerializer(obj)
    data = serializer.data


    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"datos: {data}")
    p.showPage()
    p.save()
    buffer.seek(0)
    #pdf_file = generate_pdf(data)

    response = FileResponse(buffer, as_attachment=True, filename='ticket.pdf')

    #response['Content-Disposition'] = f'attachment; filename="ticket.pdf"'

    return response

class CreateUser(generics.ListCreateAPIView):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
