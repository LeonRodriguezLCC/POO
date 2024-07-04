from gestorMiembros import GestorM
from gestorVisualizaciones import GVisualizaciones

class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                        '3':self.opcion3,
                        }
    def opcion(self,op,GM,GV):
        if type(GM)==GestorM and type(GV)==GVisualizaciones:
            fun=self.__switcher.get(op,lambda:print("Dato invalido"))
            if op=='1' or op=='2' or op =='3':
                fun(GM,GV)
            else:
                fun()
        else:
             print("Parametro invalido")
    def opcion1(self,GM,GV):
            correo=input("Ingrese el correo de un miembro\n")
            i=GM.buscarmiembro(correo)
            if i!=-1:
                 objeto=GM.darobjeto(i)
                 id=objeto.getID()
                 total=GV.TiempoTotal(id)
                 print("El usuario:\n{}\nVio un total de {} min de peliculas".format(objeto,total))
            else:
                 print("No se encontro el correo")

    def opcion2(self,GM,GV):
            GV.mostrarigual(GM)
    def opcion3(self,GM,GV):
         GM.mostrar()
         GV.mostrar()