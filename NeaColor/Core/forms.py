from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    CUIT=forms.IntegerField()
    email=forms.EmailField(max_length=50)
    domicilio = forms.CharField(max_length=100)
    codigoPostal = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'CUIT', 'email', 'domicilio', 'codigoPostal', 'telefono')
        exclude = ['username',]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'CUIT': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'domicilio': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'codigoPostal': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefono': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        }

