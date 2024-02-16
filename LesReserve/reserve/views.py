from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente
from .models import Ciudad
from .models import Departamento
from .models import Habitacion
from .models import Hotel
from .models import Personal
from .models import Reserva
from .serializers import ClienteSerializer
from .serializers import CiudadSerializer
from .serializers import DepartamentoSerializer
from .serializers import HabitacionSerializer
from .serializers import HotelSerializer
from .serializers import PersonalSerializer
from .serializers import ReservaSerializer


class ClienteView(APIView):
    def get(self, request):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)

class CiudadView(APIView):
    def get(self, request):
        queryset = Ciudad.objects.all()
        serializer = CiudadSerializer(queryset, many=True)
        return Response(serializer.data)
    
class DepartamentoView(APIView):
    def get(self, request):
        queryset = Departamento.objects.all()
        serializer = DepartamentoSerializer(queryset, many=True)
        return Response(serializer.data)
    
class HabitacionView(APIView):
    def get(self, request):
        queryset = Habitacion.objects.all()
        serializer = HabitacionSerializer(queryset, many=True)
        return Response(serializer.data)
    
class HotelView(APIView):
    def get(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PersonalView(APIView):
    def get(self, request):
        queryset = Personal.objects.all()
        serializer = PersonalSerializer(queryset, many=True)
        return Response(serializer.data)

class ReservaView(APIView):
    def get(self, request):
        queryset = Reserva.objects.all()
        serializer = ReservaSerializer(queryset, many=True)
        return Response(serializer.data)