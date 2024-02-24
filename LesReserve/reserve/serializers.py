from rest_framework import serializers
from .models import Cliente
from .models import Ciudad
from .models import Departamento
from .models import Habitacion
from .models import Hotel
from .models import Personal
from .models import Reserva

from .models import Servicio
from .models import Resena

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__' 

class HotelSerializer(serializers.ModelSerializer):
    id_ciudad = CiudadSerializer()
    class Meta:
        model = Hotel
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = '__all__' 

class HabitacionSerializer(serializers.ModelSerializer):
    id_hotel = HotelSerializer()
    class Meta:
        model = Habitacion
        fields = '__all__' 



class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__' 

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__' 