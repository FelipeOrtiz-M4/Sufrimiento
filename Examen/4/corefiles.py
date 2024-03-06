import os
import json

base = 'ejercicio_4/data/'

def checkfile(archivo, data= dict):
    if os.path.isfile(base + archivo):
        with open(base+archivo, 'r') as ar:
            data = json.load(ar)
            return data
    else:
        with open(base+archivo, 'w') as aw:
            json.dump(data, aw, indent= 4)
            return data

def updatefile(archivo, data):
    with open(base+archivo, 'r+') as awr:
        json.dump(data, awr, indent= 4)
        awr.truncate()

def searhEmpleado(nominas):
    if nominas['empleados']:
        while True:
            id= str(input(')_'))
            if id in nominas['empleados']:
                return id
            else:
                print('la id ingresada no existe')
                os.system('pause')
    else:
        print('no hay empleados\n¿A quien le piensas pagar?')
        os.system('pause')
        return