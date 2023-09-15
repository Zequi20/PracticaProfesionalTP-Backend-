from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def vista_principal(request):
    # Lógica de la vista principal
    return render(request, 'principal.html')

def vista_login(request):
    # Lógica de la vista principal
    return render(request, 'login.html')


def obtener_lista_elementos(request):
    elementos = [{'nombre': 'Elemento 1'}, {'nombre': 'Elemento 2'}]
    return JsonResponse(elementos, safe=False)
