from django.shortcuts import render
from .models import Producto
from django.views import generic


class Producto(generic.DetailView):
    template_name = 'producto.html'
    queryset = Producto.objects.all()