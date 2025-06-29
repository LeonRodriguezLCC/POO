from controladorEquipos import ControladorEquipos
from controladorResultados import ControladorResultados
def menu():
    op:int
    try:
        op=int(input("""
                            Menu
                1. Ingresar Fecha para mostrar denominacion y resultados de la fecha
                2. Ingresar equipo para mostrar resultados de cada fecha
                3. Mostrar tabla de posiciones
                0. Terminar programa
                ..."""))
    except:
        print("La respuesta debe ser un Entero sin comas")
        op=menu()
    return op
    
if __name__=='__main__':
    op:int
    CR=ControladorResultados()
    CE=ControladorEquipos()
    CR.carga()
    CE.carga()
    CR.cargarResultados(CE)
    print("                Programa de Resultados de la Liguilla")
    op=menu()
    while op!=0:
        if op==1:
            xfecha=input("Ingrese la fecha a buscar (dd/mm/aaaa):\n")
            CR.getDenominaciones(xfecha, CE)
            
            pass
        elif op==2:
            xequipo=input("Ingrese el nombre del equipo a buscar:\n")
            xidEquipo=CE.getId(xequipo)
            CR.getLocalia(xidEquipo, xequipo, CE)


            
        elif op==3:
            CE.mostrarTablaPosiciones()
        else:
            print("Opcion incorrecta")
        op=menu()
    print("                Programa Finalizado")