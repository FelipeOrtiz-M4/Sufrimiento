import os

cargos= ['Almacenista', 'Jefe IT', 'Administrador', 'Mensajero', 'Gerente']

def AddEmpleado(Nominas):
    os.system('cls')
    while True:
        id= str(input('ingrese la id del empleado :'))
        if id in Nominas:
            print('el empleado ya existe')
            os.system('pause')
            return
        else:
            break
    nombre= str(input('ingrese el nombre del empleado :'))
    os.system('cls')
    for idx, item in enumerate(cargos):
        print('estos son los cargos disponibles (seleccione 1)')
        print(f'{idx+1}, {item}')
    while True:
        try:
            op= int(input(')_'))
            cargo = cargos[op-1]
        except ValueError:
            print('no ingresaste un numero')
            os.system('pause')
        except IndexError:
            print('la opcion seleccionada no esta entre las opciones')
            os.system('pause')
        else:
            break
    os.system('cls')
    while True:
        try:
            salario= float(input('ingrese el salario del empleado :'))
        except ValueError:
            print('debes ingresar un numero ')
            os.system('pause')
        else:
            break
    empleado = {
        'id': id,
        'nombre': nombre,
        'cargo': cargo,
        'salario': salario,
        'col de pago': []
    }
    Nominas['empleados'].update({id: empleado})