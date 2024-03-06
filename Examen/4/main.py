from corefiles import checkfile
from modulos.menu import mainmenu

Nominas= {
    'empleados':{}
}
productos= checkfile('data.json', Nominas)

if __name__ == '__main__':
    mainmenu(Nominas)
    pass