import csv
from nacimiento import Nacimiento

class GestorNacimientos:
    __listaNacimientos:list

    def __init__(self):
        self.__listaNacimientos=[]

    def longLista(self):
        l=len(self.__listaNacimientos)
        return l
    
    def carga(self):
        archi=open("Nacimientos.csv")
        reader=csv.reader(archi, delimiter=";")
        next(reader)
        for fila in reader:
            nuevoNacimiento=Nacimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
            self.__listaNacimientos.append(nuevoNacimiento)
        archi.close()

    def getPosDNI(self, xdni):
        i:int=0
        pos:int=-1
        while i<len(self.__listaNacimientos) and pos==-1:
            if self.__listaNacimientos[i].getDNI()==xdni:
                pos=i
            else:
                i+=1      
        return pos

    def mostrarParto(self, xdni):
        bandera=True
        for xnacimiento in self.__listaNacimientos:
            if xnacimiento.getDNI()==xdni:
                if bandera==True:
                    if xnacimiento.getTipo()=="N":
                        tipo="normal"
                    else:
                        tipo="cesaria"
                    print(f"Tipo de parto: {tipo}\nBebe/s\n","  Peso    Altura")
                    bandera=not bandera
                print(f"{xnacimiento}")

    def mellizos(self,xdni):
        cont=0
        y:object
        bandera=True
        for x in self.__listaNacimientos:
            if x.getDNI()==xdni:
                if bandera:
                    y=x
                    bandera=False
                if x == y:
                    cont+=1
        return cont

if __name__=="__main__":
    poto=GestorNacimientos()
    poto.carga()
    poto.mostrarParto(43654654)