import os
import json

product_data = {}

def menu():
    mostra()
    while True:
        seleccion = input("Seleccione una opcion <:")
        if seleccion == "1":
            agregar_producto(product_data)
        if seleccion == "2":
            guardar(product_data)
        if seleccion == "3":
            ver()
        elif seleccion == "4":
            break

def mostra():
    print ("""
    //////////
    / usuarios /
    /////////
     """)
    print("1. agregar productos")
    print("2. Guardar cambios o productos")
    print("3. ver")
    print("4. salir")

def agregar_producto(product_data: dict):
    product_data['id'] = int(input(" ingrese el ID : "))
    product_data['nombre'] = input("ingrese el nombre del producto : ").strip()
    product_data['ValUnitario'] = input("ingrese el valor unitario <: ").strip()
    product_data['StockMin'] = input("Ingrese el stock minimo <: ").strip()
    product_data['StockMax'] = input("ingrese el stock maximo <: ").strip()


def guardar(product_data: dict, filenombre: str = "producto.json") -> None:
    with open(filenombre, "w") as f:
        json.dump(product_data, f, indent=4)
    print("Producto Agregado Correctamente!")

def cargar(filenombre: str = "productodata.json") -> dict:
    try:
        with open(filenombre, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

agregar_producto(product_data)
print(product_data)

def ver():
    print(product_data)

