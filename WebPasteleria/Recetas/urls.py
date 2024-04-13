from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def mi_vista_recetas(request):
    return HttpResponse("<h1>Recetas!</h1>")

urlpatterns = [
    path('', mi_vista_recetas), 
]