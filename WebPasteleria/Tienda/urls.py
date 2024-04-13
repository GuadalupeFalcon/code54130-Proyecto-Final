from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def mi_vista_tienda(request):
    return HttpResponse("<h1>Bienvenidos a la Tienda de Lupe!</h1>")

urlpatterns = [
    path('', mi_vista_tienda), 
]