from django import forms

from Core.models import User
from .models import Direccion, OrderItem 




class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['cantidad']

class checkForm(forms.Form):
    
    direccion = forms.CharField(required=False)
    codigoPostal = forms.CharField(required=False)
    telefono = forms.CharField(required=False)


    tipo_entrega = forms.ModelChoiceField(
        Direccion.objects.none(), required=False
    )

 

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id=user_id)

        tipo = Direccion.objects.filter(
            user=user,
            tipo_entrega= ('E', 'R')
        )

        self.fields['tipo_entrega'].queryset = tipo

        def clean(self):
            data = self.cleaned_data

            

            tipo_entrega = data.get('tipo_entrega', None)
            if tipo_entrega is None:
                if not data.get('direccion', None):
                    self.add_error("direccion", "Please fill in this field")
                if not data.get('codigoPostal', None):
                    self.add_error("codigoPostal", "Please fill in this field")
                if not data.get('telefonoE', None):
                    self.add_error("telefonao", "Please fill in this field")