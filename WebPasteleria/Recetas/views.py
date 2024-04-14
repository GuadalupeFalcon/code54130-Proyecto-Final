from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def recetas_view(request):
    return HttpResponse("<h1>Recetas!</h1>")

def search_view(request, ingrediente):
    return HttpResponse(f"<h1>A continuación se listan las recetas que incluyen {ingrediente} como ingrediente</h1>")