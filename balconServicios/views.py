from django.shortcuts import render, redirect
from .forms import FormularioCuenta
from .models import Cuentas
from .funciones import get_numero_cuenta, get_passwd
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.


def pagina_principal(request):
    return render(request, 'pagina_principal.html')


def insertar_cuenta(request):
    if request.method == 'POST':
        formulario_cuenta = FormularioCuenta(request.POST)

        if formulario_cuenta.is_valid():
            info_Form = formulario_cuenta.cleaned_data
            try:
                numero_cuenta = get_numero_cuenta(
                    Cuentas.objects.all().count(), info_Form['tipo_cuenta'])

                # print(make_password('Hola'))
                # print(check_password('Hla','pbkdf2_sha256$216000$cHNdBnXZZYXY$FTDsnNtKErK055Ml5iNwg2VWtfYyLnQZ2PvnyOwIzzg='))
                # Cuentas.objects.create(
                #     identificacion=info_Form['identificacion'], 
                #     nombre=info_Form['nombre'], 
                #     apellido=info_Form['apellido'],
                #     direccion=info_Form['direccion'],
                #     telefono=info_Form['telefono'],
                #     correo_electronico=info_Form['correo_electronico'],
                #     contrasenia=make_password(get_passwd()),
                #     numero_cuenta=numero_cuenta,
                #     tipo_cuenta=info_Form['tipo_cuenta'],
                #     saldo=0
                #     )
                messages.success(request, 'Cuenta creata con éxito')
                # return render(request, 'pagina_principal.html')
            except :
                messages.success(request, 'Algo ha ido mal!, Intentalo de nuevo')
            
    else:
        formulario_cuenta = FormularioCuenta()

    return render(request, 'insertar_cuenta.html', {'form': formulario_cuenta})
