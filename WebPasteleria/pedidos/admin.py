from django.contrib import admin
from .models import Pedido , Producto , Packaging , Avatar

# Register your models here.

admin.site.register (Pedido)
admin.site.register (Producto)
admin.site.register (Packaging)
admin.site.register (Avatar)