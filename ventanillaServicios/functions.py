

def concat_monto(dolares, centavos)->float:
    print(str(dolares)+'.'+str(centavos))
    return float(str(dolares)+'.'+str(centavos))

concat_monto('23','10')
def validar_monto(tipo:str, monto:float)->bool:
    print(tipo)
    determinante=False
    if tipo=='Ahorros' and monto <= 100.00:
        determinante=True
    elif tipo == 'Corriente'and monto <= 500:
        determinante = True
    return determinante

def generar_numero_movimiento(numero:int)->str:
    return ((9 - len(str(numero)))*'0')+str(numero+1)




