from rest_framework import serializers
from reserve.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('departamento_id', 'nombre')

"""class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('ciudad_id', 'id_departamento', 'nombre')"""