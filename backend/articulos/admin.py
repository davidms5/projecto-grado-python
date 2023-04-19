from django.contrib import admin
from .models import Tickets


class modelos(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'precio', 'uuid')

admin.site.register(Tickets, modelos)

# Register your models here.
