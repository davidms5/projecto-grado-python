from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Tickets, Empleados

class ArticuloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tickets
        fields = '__all__'


class EmpleadosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model = Empleados
        fields = ('nombre', 'apellido', 'email', 'password',)

    def create(self, validated_data):
        validated_data[password] = make_password(validated_data['password'])
        return super(ArticuloSerializer, self).create(validated_data)
