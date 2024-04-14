from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def tienda_view(request):
    return HttpResponse("<h1>Bienvenidos a la Tienda de Lupe!</h1>")