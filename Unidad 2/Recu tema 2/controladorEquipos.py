import csv
from claseEquipo import Equipo

class ControladorEquipos:
    __listaEquipos: list

    def __init__(self):
        self.__listaEquipos = []

    def agregarEquipo(self, idEquipo, denominacion, presidente, puntos, gf, gc, dg):
        equipo = Equipo(idEquipo, denominacion, presidente, puntos, gf, gc, dg)
        self.__listaEquipos.append(equipo)

    def carga(self):
        archivo=open('equiposLiguilla.csv')
        reader=csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            self.agregarEquipo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]))
        archivo.close()


    def getlistaEquipos(self):
        return self.__listaEquipos
    
    def getNombre(self, idEquipo):
        for equipo in self.__listaEquipos:
            if equipo.getIdEquipo() == idEquipo:
                return equipo.getDenominacion()
        return None

    def getId(self, denominacion):
        for equipo in self.__listaEquipos:
            if equipo.getDenominacion() == denominacion:
                return equipo.getIdEquipo()
        return None
    
    def setPuntos(self, xpuntos, gf, gc, xid):
        i=0
        flag= False
        while i < len(self.__listaEquipos) and flag == False:
            if self.__listaEquipos[i].getIdEquipo() == xid:
                xpuntos += self.__listaEquipos[i].getPuntos()
                dg = gf - gc + self.__listaEquipos[i].getDG()
                gf += self.__listaEquipos[i].getGF()
                gc += self.__listaEquipos[i].getGC()
                self.__listaEquipos[i].setPuntos(xpuntos)
                self.__listaEquipos[i].setGF(gf)
                self.__listaEquipos[i].setGC(gc)
                self.__listaEquipos[i].setDG(dg)
                flag = True
            else:
                i += 1
    
    def mostrarTablaPosiciones(self):
        self.__listaEquipos.sort(reverse=True)
        print("Posición Equipo     Puntos   Goles a Favor   Goles en Contra  Diferencia de goles")
        for i in range(len(self.__listaEquipos)):
            print (f" {i+1} {self.__listaEquipos[i].getDenominacion():<15} {self.__listaEquipos[i].getPuntos():<8} {self.__listaEquipos[i].getGF():<15} {self.__listaEquipos[i].getGC():<16} {self.__listaEquipos[i].getDG()}")
