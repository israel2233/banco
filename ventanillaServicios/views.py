from django.shortcuts import render, HttpResponse, redirect
from balconServicios.models import Cuentas
from .forms import FormularioInfoCuenta,FormularioTransaccion
from ventanillaServicios import functions
from ventanillaServicios.models import  Transacciones 


# Create your views here.
def df(request):
    flag_cuenta_valida = False
    flag_error = False
    msg_error = ''
    if request.method == 'POST':
        
        if 'montoD' in request.POST.keys():
            formulario_transac =  FormularioTransaccion(request.POST)
            concepto_t ="Transaccion Ventanilla" 
            if formulario_transac.is_valid():
                formulario_transac = formulario_transac.cleaned_data
                monto_tr = formulario_transac['montoD']+(formulario_transac['montoC']/100)
                if formulario_transac['tipo'] == 'CREDITO':
                    try:
                        saldo_actual = Cuentas.objects.get(numero_cuenta=formulario_transac['numero_cuenta']).saldo
                        cuenta_t = Cuentas.objects.filter(numero_cuenta=formulario_transac['numero_cuenta']).update(saldo=(saldo_actual+monto_tr))
                        cuenta_o = Cuentas.objects.get(numero_cuenta=formulario_transac['numero_cuenta'])

                        Transacciones.objects.create(cuenta=cuenta_o, numero_transaccion=functions.generar_numero_movimiento(Cuentas.objects.all().count()), tipo='CREDITO', concepto= concepto_t, monto= monto_tr)
                        
                        return redirect('Confirmacion')
                    except:
                        flag_error = True
                        msg_error = 'Error Inesperado'
                        return render(request,'transacciones.html',{'form':formulario_info,'flag':flag_cuenta_valida, 'flag_error':flag_error, 'msg_error':msg_error} )


                        # COLOCAR CODIGO DE ERROR
                else:
                    if functions.validar_monto(formulario_transac['tipo_cuenta'], monto_tr):

                        try:
                            saldo_actual = Cuentas.objects.get(numero_cuenta=formulario_transac['numero_cuenta']).saldo
                            if saldo_actual-monto_tr >= 0:
                                cuenta_t = Cuentas.objects.filter(numero_cuenta=formulario_transac['numero_cuenta']).update(saldo=(saldo_actual-monto_tr))
                                
                                cuenta_o = Cuentas.objects.get(numero_cuenta=formulario_transac['numero_cuenta'])

                                Transacciones.objects.create(cuenta=cuenta_o, numero_transaccion=functions.generar_numero_movimiento(Cuentas.objects.all().count()), tipo='DEBITO', concepto= concepto_t, monto= monto_tr)
                                
                                return redirect('Confirmacion')
                            else:
                                flag_error = True
                                msg_error = 'Fondos insuficientes'
                                return render(request,'transacciones.html',{'flag':flag_cuenta_valida, 'flag_error':flag_error, 'msg_error':msg_error} ) 
                        except:
                            flag_error = True
                            msg_error = 'Error Inesperado'
                            return render(request,'transacciones.html',{'flag':flag_cuenta_valida, 'flag_error':flag_error, 'msg_error':msg_error} )

                    else:
                        flag_error = True
                        msg_error = 'Monto no valido, Cuentas de Ahorro hasta 100usd y Corriente 500usd'
                        return render(request,'transacciones.html',{'flag':flag_cuenta_valida, 'flag_error':flag_error, 'msg_error':msg_error} )
                    
                    
                # ********************************************************************************************

        else:
            formulario_info =  FormularioInfoCuenta(request.POST)

            

            if formulario_info.is_valid():
                formulario_info = formulario_info.cleaned_data

                try:
                    cuenta = Cuentas.objects.get(numero_cuenta=formulario_info['numero_cuenta'])
                    formulario_info = {
                        'numero_cuenta': cuenta.numero_cuenta,
                        'nombre': cuenta.nombre,
                        'apellido': cuenta.apellido,
                        'identificacion': cuenta.identificacion,
                        'tipo_cuenta': cuenta.tipo_cuenta   
                    }
                    return render(request,'transacciones.html',{'form':formulario_info,'flag':flag_cuenta_valida,'flag_error':flag_error, 'msg_error':msg_error} )
                except :
                    msg_error = 'Cuenta no valida'
                    flag_cuenta_valida = True
                    return render(request,'transacciones.html',{'form':formulario_info,'flag':flag_cuenta_valida,'flag_error':flag_error, 'msg_error':msg_error} )
            else:
                print('No valido')


    return render(request,'transacciones.html' )


def confirm(request):
    return render(request, 'confirmacion.html')