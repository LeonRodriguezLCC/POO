from menu import menu
from gestorMiembros import GestorM
from gestorVisualizaciones import GVisualizaciones
if __name__ =='__main__':
    GM=GestorM()
    GV=GVisualizaciones()
    GM.leer()
    GV.leer()
    unmenu=menu()
    print("Bienvenido")
    op=input("Seleccione la opcion que desea\n 1-Buscar Correo\n 2-Mostrar simultaneo\n 3-Mostrar datos\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,GM,GV)
        op=input("Seleccione la opcion que desea\n 1-Buscar Correo\n 2-Mostrar simultaneo\n 3-Mostrar datos\n 0-Salir\n")
    print("Adios")