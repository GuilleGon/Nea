from django import views
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import generic
from .models import User, ConsumidorFinal
from .forms import ConsumidorSignUp, EmpresaSignUp
from django.views.generic import CreateView
from cart.models import Producto

class Index(generic.ListView):
    template_name = 'index.html'
    queryset = Producto.objects.all().order_by('-id')
    pagintate_by = 9

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = ['message'] = 'Listado de productos'

        print(context)

        return context"""

class Historial(generic.TemplateView):
    template_name = 'historial.html'

class CarritoView(generic.TemplateView):
    template_name = 'carrito.html'

class Nosotros(generic.TemplateView):
    template_name = 'nosotros.html'

class Contacto(generic.TemplateView):
    template_name = 'contacto.html'

class Blogs(generic.TemplateView):
    template_name = 'blogs.html'

class Blog(generic.TemplateView):
    template_name = 'blog.html'

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