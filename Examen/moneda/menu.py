import os

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Ingrese un numero valido.")
        except ValueError:
            print("numero invalido.")

def convert_to_yen():
    pesos = get_float_input("Ingrese el valor a cambiar ")
    yen = pesos / 26.30
    print(f"{pesos} pesos equivalente a {yen} yen.")

def convert_to_dollars():
    """Converts pesos to dollars."""
    pesos = get_float_input("Ingrese el valor a cambiar: ")
    dollars = pesos / 3944
    print(f"{pesos} pesos equivalente a {dollars} dollars.")

def convert_to_euros():
    """Converts pesos to euros."""
    pesos = get_float_input("Ingrese el valor a cambiar: ")
    euros = pesos / 43.15
    print(f"{pesos} pesos es equivalente a {euros} euros.")

def mostrar():
    print ("""
    //////////
    / moneda /
    /////////
     """)
    print("1. yen")
    print("2. dolar")
    print("3. euro")
    print("4.salir")


def menu():
    mostrar()
    while True:
        seleccion = input("Seleccione una ipcion <:")
        if seleccion == "1":
            convert_to_yen()
        if seleccion == "2":
            convert_to_dollars()
        if seleccion == "3":
            convert_to_euros()
        elif seleccion == "4":
            break


