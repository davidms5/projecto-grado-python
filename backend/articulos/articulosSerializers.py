from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Tickets, Empleados

class ArticuloSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(format='hex', read_only=True)
    
    class Meta:
        model = Tickets
        fields = ['nombre', 'apellido', 'uuid', 'fecha', 'precio']


class EmpleadosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido', 'email', 'password']

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get('password'))
        return super().create(validated_data)
