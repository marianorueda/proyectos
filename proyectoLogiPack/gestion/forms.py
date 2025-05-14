from django import forms
from .models import Paquete, Transporte

class PaqueteForm(forms.Form):
    nomdestinatario = forms.CharField(label="Nombre del destinatario", max_length=50, required=True)
    peso = forms.DecimalField(label="Peso (kg)", min_value=0.1, required=True)
    dirdestinatario = forms.CharField(label="Dirección", max_length=100, required=True)
    observaciones = forms.CharField(label="Observaciones", required=False)

class TransporteForm(forms.Form):
    paquetes = forms.ModelMultipleChoiceField(queryset=Paquete.objects.none(), widget=forms.CheckboxSelectMultiple, required=True) # pylint: disable=no-member
    def __init__(self, *args, **kwargs):
        sucursal = kwargs.pop('sucursal', None)
        super().__init__(*args, **kwargs)
        if sucursal:
            self.fields['paquetes'].queryset = Paquete.objects.filter(entregado=False, sucursal=sucursal) # pylint: disable=no-member