import modulos.usuario as us

def mainmenu(usuarios):
    while True:
        us.os.system('cls')
        print('Que deseas hacer?')
        print('1. agregar informacion de un usuario\n2. ver usarios\n3. Salir  ')
        op = str(input(')_'))
        if op == '1':
            us.addUsuario(usuarios)
        elif op == '2':
            us.tablaUser(usuarios)
        elif op == '3':
            break
        else:
            print('opcion invalida')
            us.os.system('pause')