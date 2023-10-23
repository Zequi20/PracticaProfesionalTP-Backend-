from django.shortcuts import render
#from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from reserve.models import Personal, Departamento
from reserve.serializers import PersonalSerializer, DepartamentoSerializer

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
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        departamento_data=JSONParser().parse(request)
        departamento=Departamento.objects.get(departamentoId=departamento_data['departamentoId'])
        departamento_serializer=DepartamentoSerializer(departamento,data=departamento_data)

        if departamento_serializer.is_valid():
            departamento_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        departamento=Departamento.objects.get(departamentoId=id)
        departamento.delete()
        return JsonResponse("Eliminado Correctamente",safe=False)

"""def personalApi(request,id=0):
    if request.method=='GET':
        personal = Personal.objects.all()
        personal_serializer=PersonalSerializer(personal,many=True)
        return JsonResponse(personal_serializer.data,safe=False)
    
    elif request.method=='POST':
        personal_data=JSONParser().parse(request)
        personal_serializer=PersonalSerializer(data=personal_data)

        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse("Agregado correctamente",safe=False)
        
        return JsonResponse("Error",safe=False)
    
    elif request.method=='PUT':
        personal_data=JSONParser().parse(request)
        personal=Personal.objects.get(personalId=personal_data['personalId'])
        personal_serializer=PersonalSerializer(personal,data=personal_data)

        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse("Editado Satisfactoriamente",safe=False)
        return JsonResponse("Error al modificar")
    elif request.method=='DELETE':
        personal=Personal.objects.get(personalId=id)
        personal.delete()
        return JsonResponse("Eliminado Cprrectamente",safe=False)"""
