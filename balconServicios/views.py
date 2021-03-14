from django.shortcuts import render, redirect, HttpResponse
from .forms import FormularioCuenta
from .models import Cuentas
from .funciones import get_numero_cuenta, get_passwd, get_nombre_usuario,generar_pdf
from django.contrib.auth.hashers import make_password
from django.contrib import messages



# Create your views here.


def pagina_principal(request):
    
    return render(request, 'pagina_principal.html')

def cuenta_creada(request):
    if request.method == 'POST':
        cuenta = Cuentas.objects.order_by('id').last()
        cuenta_dict ={
            'numero_cuenta': cuenta.numero_cuenta,
            'nombre': cuenta.nombre,
            'apellido': cuenta.apellido,
            'identificacion': cuenta.identificacion,
            'direccion': cuenta.direccion,
            'telefono': cuenta.telefono,
            'tipo_cuenta':cuenta.tipo_cuenta
        }
        response = HttpResponse()
        response['Content-Disposition'] = 'atachment; filename=Reporte-Cuenta.pdf'
        response.write(generar_pdf(cuenta_dict))
        return response

        

    return render(request, 'cuenta_creada.html')
    

def insertar_cuenta(request):
    
    if request.method == 'POST':
        formulario_cuenta = FormularioCuenta(request.POST)
        
        if formulario_cuenta.is_valid():
            info_Form = formulario_cuenta.cleaned_data
            try:
                numero_cuenta = get_numero_cuenta(
                    Cuentas.objects.all().count(), info_Form['tipo_cuenta'])
                contrasenia_generada = get_passwd()
                
                Cuentas.objects.create(
                    identificacion = info_Form['identificacion'],
                    nombre = info_Form['nombre'].strip().title(),
                    apellido = info_Form['apellido'].strip().title(),
                    direccion = info_Form['direccion'].strip(),
                    telefono = info_Form['telefono'].strip(),
                    correo_electronico = info_Form['correo_electronico'].strip(),
                    contrasenia = make_password(contrasenia_generada),
                    numero_cuenta = numero_cuenta,
                    tipo_cuenta = info_Form['tipo_cuenta'],
                    saldo = 0,
                    nombre_usuario = get_nombre_usuario(
                        info_Form['nombre'].strip(), info_Form['apellido'].strip())
                )
                
                return redirect('CuentaC')
            except:
                # return render(request, 'pagina_principal.html')
                messages.error(request, 'Algo ha ido mal, Intentelo nuevamente')
            
            
            
    else:
        formulario_cuenta = FormularioCuenta()

    return render(request, 'insertar_cuenta.html', {'form': formulario_cuenta})
