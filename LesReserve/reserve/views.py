from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage

from django.shortcuts import render
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
        return JsonResponse(" Eliminado Correctamente ",safe=False)
    
@api_view(['POST'])
def SaveFile(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        # Provide a relative path for the file within the storage system
        file_path = default_storage.save(f"uploads/{file.name}", file)
        return Response({"mensaje": "Archivo guardado correctamente", "nombre_archivo": file_path})
    else:
        return Response({"error": "No se encontró ningún archivo en la solicitud"}, status=400)

""" django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from reserve.models import Departamento, Ciudad 
from reserve.serializers import  DepartamentoSerializer , CiudadSerializer

@method_decorator(csrf_exempt, name='dispatch')
class DepartamentoView(View):
    def get(self, request, *args, **kwargs):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        departamento_data = JSONParser().parse(request)
        serializer = DepartamentoSerializer(data=departamento_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Agregado correctamente", safe=False)

        return JsonResponse("Error", safe=False)

    def put(self, request, *args, **kwargs):
        departamento_data = JSONParser().parse(request)
        departamento = Departamento.objects.get(departamentoId=departamento_data['departamentoId'])
        serializer = DepartamentoSerializer(departamento, data=departamento_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Editado Satisfactoriamente", safe=False)
        return JsonResponse("Error al modificar", safe=False)

    def delete(self, request, *args, **kwargs):
        departamento = Departamento.objects.get(departamentoId=kwargs['id'])
        departamento.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)"""
