from django.shortcuts import render
from django.http import HttpResponse

def vista_principal(request):
    # Lógica de la vista principal
    return render(request, 'principal.html')

def vista_login(request):
    # Lógica de la vista principal
    return render(request, 'login.html')
