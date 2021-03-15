from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from balconServicios.models import Cuentas
from ventanillaServicios.models import Transacciones
from django.template import loader
from datetime import date, datetime
from ventanillaServicios import functions
# Create your views here.

def login(request):
    error_flag = False
    error_msj = ''
    if request.method == 'POST':
        try:
            
            cuenta_login = Cuentas.objects.get(nombre_usuario=request.POST['nombre_usuario'])
            # Comprobar contrasenia
            if check_password(request.POST['passwd'], cuenta_login.contrasenia):
                return consolidado(request, cuenta_login.numero_cuenta)
            else:
                print('s')
                error_flag = True
                error_msj = 'Credenciales no validas'
                return render(request, 'login.html',{'error_flag':error_flag, 'error_msj': error_msj })

        except Cuentas.DoesNotExist:
            print('sa')
            error_flag = True
            error_msj = 'Credenciales no validas'
            return render(request, 'login.html',{'error_flag':error_flag, 'error_msj': error_msj })
    return render(request, 'login.html')

def consolidado(request, numero_cuenta):
    print(numero_cuenta)
    info = Cuentas.objects.get(numero_cuenta=numero_cuenta)
    context = {
        'nombres': "{} {}".format(info.nombre, info.apellido),
        'numero_cuenta': numero_cuenta,
        'saldo': info.saldo
        }

    return render(request, 'consolidado.html', context)

def historial(request, cuenta):
    # print(request.GET['cuenta'])
    
    cuenta_mov = Cuentas.objects.get(numero_cuenta=cuenta) 
    movimientos = Transacciones.objects.filter(cuenta=cuenta_mov)
    lista_movimientos = []
    for movimiento in movimientos:
        # print(type(date.isoformat(movimiento.fecha)))
        if movimiento.tipo == 'CREDITO':
            mov_tipo_impresion = '+'
        else:
            mov_tipo_impresion = '-'
        lista_movimientos.append({
            'fecha': date.isoformat(movimiento.fecha),
            'numero_transaccion': movimiento.numero_transaccion,
            'tipo': mov_tipo_impresion,
            'concepto': movimiento.concepto,
            'monto': movimiento.monto
        })

    return render(request, 'historial.html',{'movimientos':lista_movimientos})

def transaccion(request, cuenta):
    flag_error = False
    msj_error= ''
    if request.method == 'POST':
        busqueda = Cuentas.objects.filter(numero_cuenta=request.POST['cuenta_destino'])
        cuenta_dest = busqueda[0]
        cuenta_orig = Cuentas.objects.get(numero_cuenta=cuenta)

        if len(busqueda)==0:
            flag_error = True
            msj_error = 'Cuenta invalida'
            return render(request, 'transacciones_banca.html',{'flag_error':flag_error, 'msj_error':msj_error})
        cuenta_dest = busqueda[0]
        monto = float(request.POST['montoD'])+ (float(request.POST['montoC'])/100)
        
        if cuenta_orig.saldo - monto < 0 :
            flag_error = True
            msj_error = 'Saldo insuficiente'
            return render(request, 'transacciones_banca.html',{'flag_error':flag_error, 'msj_error':msj_error})
        try:
            Cuentas.objects.filter(numero_cuenta=request.POST['cuenta_destino']).update(saldo=(cuenta_dest.saldo + monto))
            Cuentas.objects.filter(numero_cuenta=cuenta).update(saldo=cuenta_orig.saldo - monto)
            # Generar registro
            numero_transaccion = functions.generar_numero_movimiento(Transacciones.objects.all().count())
            Transacciones.objects.create(cuenta=cuenta_orig, tipo='DEBITO', concepto=request.POST['concepto'], monto=monto, numero_transaccion= numero_transaccion)
            numero_transaccion = functions.generar_numero_movimiento(Transacciones.objects.all().count())
            Transacciones.objects.create(cuenta=cuenta_dest, tipo='CREDITO', concepto=request.POST['concepto'], monto=monto, numero_transaccion= numero_transaccion)
            print('si')
            return redirect('/confirmacion')

        except:
            flag_error = True
            msj_error = 'Error interno'
            return render(request, 'transacciones_banca.html',{'flag_error':flag_error, 'msj_error':msj_error})


        

    return render(request, 'transacciones_banca.html')


def confirm(request):
    return render(request, 'confirmacion.html')