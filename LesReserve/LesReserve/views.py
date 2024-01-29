from django.shortcuts import render
#from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from reserve.models import Departamento, Ciudad 
from reserve.serializers import  DepartamentoSerializer , CiudadSerializer

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
