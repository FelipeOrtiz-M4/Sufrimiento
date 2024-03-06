import os
from tabulate import tabulate

def addUsuario(usuarios):
    os.system('cls')
    while True:
        id= str(input('ingrese la id del usuario :'))
        if id in usuarios:
            print('el usuario ya existe')
            os.system('pause')
            return
        else:
            break
    nombres= str(input('ingrese los nombres del usuario :'))
    apellidos= str(input('ingrese los apellidos del usuario :'))
    direccion= str(input('ingrese la direccion del usuario :'))
    ciudad= str(input('ingrese la ciudad del usuario :'))
    while True:
        try:
            longitud= float(input('ingrese la longitud del usuario :'))
            latitud= float(input('ingrese la latitud del usuario :'))
        except ValueError:
            print('la longitud o la latitud ingresadas no son un numero ')
            os.system('pause')
        else:
            break
    email= str(input('ingrese el email del usuario :'))
    while True:
        try:
            edad= int(input('ingrese la edad del usuario :'))
        except ValueError:
            print('la edad debe ser un numero entero ')
            os.system('pause')
        else:
            break
    ocupacion= str(input('ingrese la ocupacion del usuario :'))
    usuario = {
        'id': id,
        'nombres': nombres,
        'apellidos': apellidos,
        'ubicacion': {
            'direccion': direccion,
            'ciudad': ciudad,
            'longitud': longitud,
            'latitud': latitud
        },
        'email': email,
        'edad': edad,
        'ocupacion': ocupacion
        
    }
    usuarios.update({id: usuario})
    
def tablaUser(usuarios):
    tabla = []
    for values in usuarios.values():
        tabla.append(values)
    print(tabulate(tabla, headers= 'keys', tablefmt='grid'))
    os.system('pause')