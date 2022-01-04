from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ConsumidorFinal, Empresa
from django.db import transaction
    
class ConsumidorSignUp(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    cuit = forms.IntegerField(required=True)
    domicilio = forms.CharField(required=True)
    codigoPostal = forms.IntegerField(required=True)
    telefono = forms.CharField(required=True)
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'cuit', 'email', 'domicilio', 'codigoPostal', 'telefono')
        exclude = ['username',]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.cuit = self.cleaned_data.get('cuit')
        user.domicilio = self.cleaned_data.get('domicilio')
        user.codigoPostal = self.cleaned_data.get('codigoPostal')
        user.telefono = self.cleaned_data.get('telefono')
        user.is_consumidor = True
        user.save()
        consumidor = ConsumidorFinal.objects.create(user=user)
        consumidor.nombre = self.cleaned_data.get('nombre')
        consumidor.apellido = self.cleaned_data.get('apellido')
        consumidor.save()
        return user


class EmpresaSignUp(UserCreationForm):
    razonSocial = forms.CharField(max_length=100, required=True)
    rubro = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    cuit = forms.IntegerField(required=True)
    domicilio = forms.CharField(required=True)
    codigoPostal = forms.IntegerField(required=True)
    telefono = forms.CharField(required=True)
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('razonSocial', 'rubro', 'cuit', 'email', 'domicilio', 'codigoPostal', 'telefono')
        exclude = ['username',]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.cuit = self.cleaned_data.get('cuit')
        user.domicilio = self.cleaned_data.get('domicilio')
        user.codigoPostal = self.cleaned_data.get('codigoPostal')
        user.telefono = self.cleaned_data.get('telefono')
        user.is_empresa = True
        user.save()
        empresa = Empresa.objects.create(user=user)
        empresa.razonSocial = self.cleaned_data.get('razonSocial')
        empresa.rubro = self.cleaned_data.get('rubro')
        empresa.save()
        return user