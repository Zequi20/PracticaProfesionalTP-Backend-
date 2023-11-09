from django.shortcuts import render
#from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from reserve.models import Personal, Departamento, Ciudad, Cliente, Hotel, Habitacion, Servicio, Reserva, Resena 
from reserve.serializers import PersonalSerializer, DepartamentoSerializer , CiudadSerializer, ClienteSerializer, HotelSerializer, HabitacionSerializer, ServicioSerializer, ReservaSerializer, ResenaSerializer

@csrf_exempt
def departamentoApi(request,id=0):
    if request.method=='GET':
        departamento = Departamento.objects.all()
        departamento_serializer=DepartamentoSerializer(departamento,many=True)
        return JsonResponse(departamento_serializer.data,safe=False)
    
    elif request.method=='POST':
        departamento_data=JSONParser().parse(request)
        departamento_serializer=DepartamentoSerializer(data=departamento_data)

        if departamento_serializer.is_valid():
            departamento_serializer.save()
            return JsonResponse(" Agregado correctamente ",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        departamento_data=JSONParser().parse(request)
        departamento=Departamento.objects.get(departamentoId=departamento_data['departamentoId'])
        departamento_serializer=DepartamentoSerializer(departamento,data=departamento_data)

        if departamento_serializer.is_valid():
            departamento_serializer.save()
            return JsonResponse(" Editado Satisfactoriamente ",safe=False)
        return JsonResponse(" Error al modificar ")
    elif request.method=='DELETE':
        departamento=Departamento.objects.get(departamentoId=id)
        departamento.delete()
        return JsonResponse("Eliminado Correctamente",safe=False)

def personalApi(request,id=0):
    if request.method=='GET':
        personal = Personal.objects.all()
        personal_serializer=PersonalSerializer(personal,many=True)
        return JsonResponse(personal_serializer.data,safe=False)
    
    elif request.method=='POST':
        personal_data=JSONParser().parse(request)
        personal_serializer=PersonalSerializer(data=personal_data)

        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse(" Agregado correctamente ",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        personal_data=JSONParser().parse(request)
        personal=Personal.objects.get(personalId=personal_data['personalId'])
        personal_serializer=PersonalSerializer(personal,data=personal_data)

        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse(" Editado Satisfactoriamente ",safe=False)
        return JsonResponse(" Error al modificar ")
    elif request.method=='DELETE':
        personal=Personal.objects.get(personalId=id)
        personal.delete()
        return JsonResponse(" Eliminado Cprrectamente ",safe=False)
    
def ciudadApi(request,id=0):
    if request.method=='GET':
        ciudad = Ciudad.objects.all()
        ciudad_serializer=CiudadSerializer(ciudad,many=True)
        return JsonResponse(ciudad_serializer.data,safe=False)
    
    elif request.method=='POST':
        ciudad_data=JSONParser().parse(request)
        ciudad_serializer=CiudadSerializer(data=ciudad_data)

        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        ciudad_data=JSONParser().parse(request)
        ciudad=Ciudad.objects.get(ciudadId=ciudad_data['ciudadId'])
        ciudad_serializer=CiudadSerializer(ciudad,data=ciudad_data)

        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JsonResponse(" Editado Satisfactoriamente ",safe=False)
        return JsonResponse(" Error al modificar ")
    elif request.method=='DELETE':
        ciudad=Ciudad.objects.get(ciudadId=id)
        ciudad.delete()
        return JsonResponse(" Eliminado Cprrectamente ",safe=False)
    
def clienteApi(request,id=0):
    if request.method=='GET':
        cliente = Cliente.objects.all()
        cliente_serializer=ClienteSerializer(cliente,many=True)
        return JsonResponse(cliente_serializer.data,safe=False)
    
    elif request.method=='POST':
        cliente_data=JSONParser().parse(request)
        cliente_serializer=ClienteSerializer(data=cliente_data)

        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        cliente_data=JSONParser().parse(request)
        cliente=Cliente.objects.get(clienteId=cliente_data['clienteId'])
        cliente_serializer=ClienteSerializer(cliente,data=cliente_data)

        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        cliente=Cliente.objects.get(clienteId=id)
        cliente.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)
    

def hotelApi(request,id=0):
    if request.method=='GET':
        hotel = Hotel.objects.all()
        hotel_serializer=HotelSerializer(hotel,many=True)
        return JsonResponse(hotel_serializer.data,safe=False)
    
    elif request.method=='POST':
        hotel_data=JSONParser().parse(request)
        hotel_serializer=HotelSerializer(data=hotel_data)

        if hotel_serializer.is_valid():
            hotel_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        hotel_data=JSONParser().parse(request)
        hotel=Hotel.objects.get(hotelId=hotel_data['hotelId'])
        hotel_serializer=HotelSerializer(hotel,data=hotel_data)

        if hotel_serializer.is_valid():
            hotel_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        hotel=Hotel.objects.get(hotelId=id)
        hotel.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)

def habitacionApi(request,id=0):
    if request.method=='GET':
        habitacion = Habitacion.objects.all()
        habitacion_serializer=HabitacionSerializer(habitacion,many=True)
        return JsonResponse(habitacion_serializer.data,safe=False)
    
    elif request.method=='POST':
        habitacion_data=JSONParser().parse(request)
        habitacion_serializer=HabitacionSerializer(data=habitacion_data)

        if habitacion_serializer.is_valid():
            habitacion_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        habitacion_data=JSONParser().parse(request)
        habitacion=Habitacion.objects.get(habitacionlId=habitacion_data['habitacionId'])
        habitacion_serializer=HabitacionSerializer(habitacion,data=habitacion_data)

        if habitacion_serializer.is_valid():
            habitacion_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        habitacion=Habitacion.objects.get(habitacionId=id)
        habitacion.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)

def servicioApi(request,id=0):
    if request.method=='GET':
        servicio = Servicio.objects.all()
        servicio_serializer=ServicioSerializer(servicio,many=True)
        return JsonResponse(servicio_serializer.data,safe=False)
    
    elif request.method=='POST':
        servicio_data=JSONParser().parse(request)
        servicio_serializer=ServicioSerializer(data=servicio_data)

        if servicio_serializer.is_valid():
            servicio_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        servicio_data=JSONParser().parse(request)
        servicio=Servicio.objects.get(servicioId=servicio_data['servicioId'])
        servicio_serializer=ServicioSerializer(servicio,data=servicio_data)

        if servicio_serializer.is_valid():
            servicio_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        servicio=Servicio.objects.get(servicioId=id)
        servicio.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)
    

def ReservaApi(request,id=0):
    if request.method=='GET':
        reserva = Reserva.objects.all()
        reserva_serializer=ReservaSerializer(reserva,many=True)
        return JsonResponse(reserva_serializer.data,safe=False)
    
    elif request.method=='POST':
        reserva_data=JSONParser().parse(request)
        reserva_serializer=ReservaSerializer(data=reserva_data)

        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        reserva_data=JSONParser().parse(request)
        reserva=Reserva.objects.get(reservaId=reserva_data['reservaId'])
        reserva_serializer=ReservaSerializer(reserva,data=reserva_data)

        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        reserva=Reserva.objects.get(reservaId=id)
        reserva.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)

def ResenaApi(request,id=0):
    if request.method=='GET':
        resena = Resena.objects.all()
        resena_serializer=ResenaSerializer(resena,many=True)
        return JsonResponse(resena_serializer.data,safe=False)
    
    elif request.method=='POST':
        resena_data=JSONParser().parse(request)
        resena_serializer=ResenaSerializer(data=resena_data)

        if resena_serializer.is_valid():
            resena_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        resena_data=JSONParser().parse(request)
        resena=Resena.objects.get(resenaId=resena_data['resenaId'])
        resena_serializer=ResenaSerializer(resena,data=resena_data)

        if resena_serializer.is_valid():
            resena_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        resena=Resena.objects.get(resenaId=id)
        resena.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)
