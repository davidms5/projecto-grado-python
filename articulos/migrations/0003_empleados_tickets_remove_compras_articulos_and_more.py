# Generated by Django 4.2 on 2023-04-15 04:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("articulos", "0002_compras"),
    ]

    operations = [
        migrations.CreateModel(
            name="Empleados",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Tickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("apellido", models.CharField(max_length=200)),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(model_name="compras", name="articulos",),
        migrations.DeleteModel(name="Articulo",),
        migrations.DeleteModel(name="Compras",),
    ]