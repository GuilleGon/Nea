from django.contrib import admin
from .models import Producto, Orden, OrderItem
# Register your models here.

admin.site.register(Producto)
admin.site.register(OrderItem)
admin.site.register(Orden)