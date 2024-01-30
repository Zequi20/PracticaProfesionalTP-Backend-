from rest_framework import serializers
from reserve.models import Departamento,  Ciudad


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields=('departamentoId','nombre')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudad
        fields=('ciudadId','departamentoId','nombre')