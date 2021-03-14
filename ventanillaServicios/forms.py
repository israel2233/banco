from django import forms

class FormularioTransaccion(forms.Form):
    numero_cuenta = forms.CharField(max_length=7, min_length=7, required=True)
    tipo = forms.CharField(required=True)
    montoD = forms.FloatField(min_value=0, max_value=500)
    montoC = forms.FloatField(max_value=99)
    tipo_cuenta = forms.CharField(required=False)
    
class FormularioInfoCuenta(forms.Form):
    numero_cuenta = forms.CharField()
    identificacion = forms.CharField(required=False)
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    tipo_cuenta = forms.CharField(required=False)