from django.contrib import admin
from .models import ConsumidorFinal, Empresa, User
from cart.models import Producto

admin.site.register(User)
admin.site.register(ConsumidorFinal)
admin.site.register(Empresa)