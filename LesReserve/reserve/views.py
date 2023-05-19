from django.shortcuts import render


def vista_principal(request):
   
    return render(request, 'templates/index.html')
