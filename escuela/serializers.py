from rest_framework import serializers
from .models import Alumno, Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('id', 'nombre')

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'carrera')