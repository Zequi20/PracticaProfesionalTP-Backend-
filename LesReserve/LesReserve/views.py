from django.shortcuts import render
from django.http import HttpResponse

def vista_principal(request):
    # Lógica de la vista principal
    return render(request, 'principal.html')

def vista1(request):
    # Lógica de la vista 1
    return HttpResponse("Vista 1")

def vista2(request):
    # Lógica de la vista 2
    return HttpResponse("Vista 2")
