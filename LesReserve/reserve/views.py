from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .models import Ciudad
from .models import Departamento
from .models import Habitacion
from .models import Hotel
from .models import Personal
from .models import Reserva

from .models import Servicio
from .models import Resena



from .serializers import ClienteSerializer
from .serializers import CiudadSerializer
from .serializers import DepartamentoSerializer
from .serializers import HabitacionSerializer
from .serializers import HotelSerializer
from .serializers import PersonalSerializer
from .serializers import ReservaSerializer

from .serializers import ServicioSerializer
from .serializers import ResenaSerializer




class ClienteView(APIView):
    def get(self, request):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            data = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CiudadView(APIView):
    def get(self, request):
        queryset = Ciudad.objects.all()
        serializer = CiudadSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            data = Ciudad.objects.get(pk=pk)
        except Ciudad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DepartamentoView(APIView):
    def get(self, request):
        queryset = Departamento.objects.all()
        serializer = DepartamentoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            data = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HabitacionView(APIView):
    def get(self, request):
        queryset = Habitacion.objects.all()
        serializer = HabitacionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HabitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUE)
    
    def delete(self, request, pk):
        try:
            data = Habitacion.objects.get(pk=pk)
        except Habitacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HotelView(APIView):
    def get(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUE)
    
    def delete(self, request, pk):
        try:
            data = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PersonalView(APIView):
    def get(self, request):
        queryset = Personal.objects.all()
        serializer = PersonalSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUE)
    
    def delete(self, request, pk):
        try:
            data = Personal.objects.get(pk=pk)
        except Personal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReservaView(APIView):
    def get(self, request):
        queryset = Reserva.objects.all()
        serializer = ReservaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        id_cliente = request.data.get('id_cliente')  # Obtener el ID del cliente del cuerpo de la solicitud
        reservas = Reserva.objects.filter(id_cliente=id_cliente)  # Filtrar las reservas por ID de cliente
        serializer = ReservaSerializer(reservas, many=True)  # Serializar las reservas encontradas
        return Response(serializer.data)  # Retornar las reservas encontradas
    
    def create(self, request):
        serializer = ReservaSerializer(data=request.data)  # Crear un serializador con los datos de la solicitud
        if serializer.is_valid():  # Verificar si los datos son válidos
            serializer.save()  # Guardar la reserva en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retornar los datos de la reserva creada
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retornar errores si los datos no son válidos

    def delete(self, request, pk):
        try:
            data = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class ServicioView(APIView):
    def get(self, request):
        queryset = Servicio.objects.all()
        serializer = ServicioSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUE)
    
    def delete(self, request, pk):
        try:
            data = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ResenaView(APIView):
    def get(self, request):
        queryset = Resena.objects.all()
        serializer = ResenaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ResenaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUE)
    
    def delete(self, request, pk):
        try:
            data = Resena.objects.get(pk=pk)
        except Resena.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoginView(APIView):
    def post(self, request):
        usuario = request.data.get('usuario')
        clave = request.data.get('clave')
        
        try:
            cliente = Cliente.objects.get(nombre=usuario)
        except Cliente.DoesNotExist:
            return Response({'success': False, 'message': 'Usuario no encontrado'})
        
        if cliente.clave == clave:
            serializer = ClienteSerializer(cliente)
            return Response({'success': True, 'cliente': serializer.data})
        else:
            return Response({'success': False, 'message': 'Clave incorrecta'})

