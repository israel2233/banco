from django import forms

class FormularioCuenta(forms.Form):
    identificacion = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    correo_electronico = forms.EmailField()
    tipo_cuenta = forms.CharField()
    