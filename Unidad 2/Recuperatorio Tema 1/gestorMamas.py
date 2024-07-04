import numpy as np
import csv
from mama import Mama
class GestorMamas:
    __incremento:int
    __cantidad:int
    __dimension:int
    __listaMamas:np.ndarray
    def __init__(self):
        self.__dimension=20
        self.__incremento=5
        self.__cantidad=0
        self.__listaMamas=np.empty(self.__dimension, dtype=Mama)
    
    def agregar(self, nuevaMama):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__listaMamas.resize(self.__dimension)
        self.__listaMamas[self.__cantidad]=nuevaMama
        self.__cantidad+=1

    def carga(self):
        archi=open("Mamas.csv")
        reader=csv.reader(archi, delimiter=";")
        next(reader)
        for fila in reader:
            nuevaMama=Mama(int(fila[0]), int(fila[1]), fila[2])
            self.agregar(nuevaMama)
        archi.close()

    def getPosDNI(self, xdni):
        i:int=0
        pos:int=-1
        while i<len(self.__listaMamas) and pos==-1:
            if self.__listaMamas[i].getDNI()==xdni:
                pos=i
            else:
                i+=1
        return pos

    def mostrarParto(self, xdni):
        i=0
        while self.__listaMamas[i].getDNI()!=xdni and i<len(self.__listaMamas):
            i+=1
        if i<len(self.__listaMamas):
            print(f"""
{self.__listaMamas[i]}""")
        else:
            print("no se encontro el dni")
    
    def getDNI(self, i):
        return self.__listaMamas[i].getDNI()
    def getAyn(self, i):
        return self.__listaMamas[i].getAyn()
    def getEdad(self, i):
        return self.__listaMamas[i].getEdad()
    def getLong(self):
        return self.__cantidad
    
if __name__=="__main__":
    poto=GestorMamas()
    poto.carga()
    poto.mostrarParto(35898561)