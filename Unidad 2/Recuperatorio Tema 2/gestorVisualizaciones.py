import csv
from visualizacion import visualizacion
class GVisualizaciones():
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def leer(self):
        archivo=open("Visualizaciones.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unavisualizacion=visualizacion(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unavisualizacion)

        archivo.close()
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    def TiempoTotal(self,id):
        total=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getIDM()==id:
                total+=self.__lista[i].getDuracion()
        return total
    def mostrarigual(self,GM):
        listado=[]
        for i in range(len(self.__lista)):
            j=0
            band=True
            for j in range (len(self.__lista)):
                if j==i:
                    band=False
                elif(self.__lista[i]==self.__lista[j]):
                    posicion=GM.buscarmiembro(self.__lista[i].getIDM())
                    objeto1=GM.darobjeto(posicion)
                    posicion=GM.buscarmiembro(self.__lista[j].getIDM())
                    objeto2=GM.darobjeto(posicion)
                    k=0
                    while k<len(listado) and listado[k].getID()!=objeto1.getID():
                       k+=1
                    if k>=len(listado):
                        print("El usuario {}{}\nY el usuario {}{}\nVieron simultaneamente\n".format(objeto1.getNombre(),objeto1.getEmail(),objeto2.getNombre(),objeto2.getEmail()))
                        listado.append(objeto1)