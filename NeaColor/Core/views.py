from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class Nosotros(generic.TemplateView):
    template_name = 'nosotros.html'

class Contacto(generic.TemplateView):
    template_name = 'contact.html'


def RegistroConsumidorFinal(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            login(request, user, backend='Core.backends.EmailBackend')
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data['form'] = formulario

    return render(request, 'registration/registration.html', data)
