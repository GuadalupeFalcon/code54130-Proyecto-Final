
from django.contrib import admin
from django.urls import path
from .views import recetas_view, search_view

urlpatterns = [
    path('', recetas_view), 
    path("buscar/<ingrediente>", search_view), 
] 