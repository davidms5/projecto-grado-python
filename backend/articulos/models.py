from django.db import models
import uuid
#from django.contrib.auth.hashers import make_password
# Create your models here.

class Tickets(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.nombre

#
#
# lo de anajo es basicamente para el login del frontend
#
#
class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=128)


#class Articulo(models.Model):
#    codigo = models.CharField(max_length=200)
#    nombre = models.CharField(max_length=200)
#    precio = models.DecimalField(max_digits=10, decimal_places=2)
#    cantidad = models.IntegerField(help_text="insertar cantidad")
#
#    def __str__(self):
#        return self.nombre

#class Compras(models.Model):
#
#    compra_date = models.DateTimeField(auto_now_add=True)
#    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#    articulos = models.ManyToManyField(Articulo)
#    total = models.DecimalField(max_digits=10, decimal_places=2)
#
#    def __str__(self):
#        return f"compra {self.uuid}"
#
#    def total_cost(self):
#        return sum(articulo.precio for articulo in self.articulos.all())

