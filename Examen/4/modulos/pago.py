import os
from corefiles import searhEmpleado

def PagarEmpleado(Nominas):
    print('estas son los empleados existentes\nA cual le quieres pagar?')
    for key, value in Nominas['empleados']:
        print(f'{key}, {value["nombre"]}')
    id = searhEmpleado()
    