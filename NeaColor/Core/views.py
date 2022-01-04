from django import views
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import generic
from .models import User, ConsumidorFinal
from .forms import ConsumidorSignUp, EmpresaSignUp
from django.views.generic import CreateView
from cart.models import Producto


class HomeView(generic.ListView):
    template_name = 'index.html'
    queryset = Producto.objects.all()


class Nosotros(generic.TemplateView):
    template_name = 'nosotros.html'

class Contacto(generic.TemplateView):
    template_name = 'contact.html'


class RegistroConsumidorFinal(CreateView):
    model = User
    form_class = ConsumidorSignUp
    template_name = 'registration/registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ConsumidorFinal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class RegistroEmpresa(CreateView):
    model = User
    form_class = EmpresaSignUp
    template_name = 'registration/registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Empresa'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('home')