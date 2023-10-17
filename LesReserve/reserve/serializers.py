from rest_framework import serializers
from reserve.models import Departamento, Personal, Ciudad, Cliente, Hotel, Habitacion, Servicio, Reserva, Resena


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields=('departamentoId','nombre')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudad
        fields=('ciudadId','id_departamento','nombre')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('clienteId','nombre','apellido','id_ciudad','correo','telefono','fecha_inicio','ci','estado','direccion','foto')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=('hotelId','nombre','direccion','telefono','correo','id_ciudad','estado')

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Habitacion
        fields=('habitacionId','id_hotel','tipo','numero','precio','descripcion','foto','capacidad','estado')


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal
        fields=('personalId','nombre','apellido','fecha_alta','id_hotel','puesto','ci','telefono','correo','fecha_nacimiento','id_ciudad','estado','foto')

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields=('servicioId','precio','servicio_tipo','detalle')
       
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reserva
        fields=('reservaId','id_cliente','id_servicio','id_habitacion','id_personal','cantidad','fecha_inicio','fecha_fin','estado','observacion')

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resena
        fields=('resenaId','id_hotel','id_cliente','comentario')