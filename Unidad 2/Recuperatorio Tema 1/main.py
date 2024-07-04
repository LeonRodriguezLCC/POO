from gestorMamas import GestorMamas
from gestorNacimientos import GestorNacimientos

def menu():
    op:int
    try:
        op=int(input("""
                            Menu
                1. Ingresar DNI para mostrar informacion del parto
                2. Mostrar datos de mamas con parto multiple
                0. Terminar programa
                ..."""))
    except:
        print("La respuesta debe ser un Entero sin comas")
        op=menu()
    return op
    
if __name__=='__main__':
    op:int
    GM=GestorMamas()
    GN=GestorNacimientos()
    GM.carga()
    GN.carga()
    op=menu()
    while op!=0:
        if op==1:
            xdni=int(input("ingrese el dni de la madre: "))
            GM.mostrarParto(xdni)
            GN.mostrarParto(xdni)
        elif op==2:
            print("Las mamas que han tenido parto múltiple son:\n")
            for i in range(GM.getLong()):
                xdni=GM.getDNI(i)
                bebes=GN.mellizos(xdni)
                if bebes>1:
                    ayn=GM.getAyn(i)
                    edad=GM.getEdad(i)
                    print(f"DNI: {xdni}\nApellido y Nombre: {ayn}\nEdad: {edad}\n")
        else:
            print("Opcion incorrecta")
        op=menu()