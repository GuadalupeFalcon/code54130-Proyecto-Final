from django.contrib import admin
from django.urls import path
from .views import tienda_view


urlpatterns = [
    path('', tienda_view), 
]