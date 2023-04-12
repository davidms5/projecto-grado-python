from django.db import models
import uuid
# Create your models here.

class Articulo(models.Model):
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(help_text="insertar cantidad")

    def __str__(self):
        return self.nombre

class Compras(models.Model):

    compra_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    articulos = models.ManyToManyField(Articulo)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"compra {self.uuid}"

    def total_cost(self):
        return sum(articulo.precio for articulo in self.articulos.all())

