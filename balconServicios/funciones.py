from random import choice

def get_numero_cuenta(numero:int, tipo:str )->str:
    numero += 1
    cuenta = 'CC'
    if tipo == 'Ahorros':
        cuenta = 'CA'
   

    return cuenta + ( ( 5 - len( str(numero) ) )*'0')+str(numero) #Genera el string del numero de cuenta

def get_passwd():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    password = password.join([choice(alfabeto) for i in range(8)])
    return password

def get_nombre_usuario(nombre:str, apellido:str)->str:
    return (nombre[0]+apellido).upper()

print(get_nombre_usuario('Hola', 'Juarez'))