from django import forms

from Core.models import User
from .models import Direccion, OrderItem, Pago 


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['cantidad']

class checkForm(forms.Form):
    
    direccion = forms.CharField(required=False)
    codigoPostal = forms.CharField(required=False)
    telefono = forms.CharField(required=False)

    class Meta:
        model = Pago
        fields = ['direccion']
