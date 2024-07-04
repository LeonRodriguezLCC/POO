import numpy as np
import csv
from miembro import miembro
class GestorM():
    __incremento:int
    __cantidad:int
    __miembros:np.ndarray
    __dimension:int
    def __init__(self,dimension=20) -> None:
        self.__dimension=dimension
        self.__incremento=10
        self.__cantidad=0
        self.__miembros=np.empty(self.__dimension,dtype=miembro)
    def agregar(self,unmiembro):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__miembros.resize(self.__dimension)
        self.__miembros[self.__cantidad]=unmiembro
        self.__cantidad+=1
    def leer(self):
        archivo=open("Miembros.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unmiembro=miembro(fila[0],fila[1],fila[2])
                self.agregar(unmiembro)
        archivo.close()
    def mostrar(self):
        for i in range(len(self.__miembros)):
            if self.__miembros[i]!=None and self.__miembros[i]!=0:
                print(self.__miembros[i])

    def buscarmiembro(self,dato):
        posicion=-1
        if type(dato)==int: 
            posicion=self.buscarID(dato)
        else:
            posicion=self.buscarCorreo(dato)
        return posicion

    def buscarID(self,ID):
        posicion=-1
        i=0
        while i<len(self.__miembros) and posicion==-1:
            if self.__miembros[i]!=None and self.__miembros[i]!=0:
                if self.__miembros[i].getID()==ID:
                    posicion=i
            i+=1
  
        return posicion
    def buscarCorreo(self,correo):
        posicion=-1
        i=0
        while i<len(self.__miembros) and posicion==-1:
            if self.__miembros[i]!=None and self.__miembros[i]!=0:
                if self.__miembros[i].getEmail()==correo:
                    posicion=i
            i+=1
  
        return posicion
    def darobjeto(self,i):
        return self.__miembros[i]