from rest_framework import serializers
from escola.models import Estudante, Curso 

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        filds = '__all__'


class CursoSerializar(serializers.ModelSerializer):
    class Meta:
        model = Curso
        filds = '__all__'