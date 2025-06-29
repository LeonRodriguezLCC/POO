import csv
import numpy as np
from claseResultado import Resultado

class ControladorResultados:
    __incremento: int
    __cantidad: int
    __dimension: int
    __listaResultados: np.ndarray

    def __init__(self):
        self.__incremento=2
        self.__cantidad=0
        self.__dimension=16
        self.__listaResultados = np.empty(self.__dimension, dtype=Resultado)

    def agregar(self, unResultado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaResultados.resize(self.__dimension)
        self.__listaResultados[self.__cantidad] = unResultado
        self.__cantidad += 1
    
    def carga(self):
        archivo = open('resultadosLiguilla.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            nuevoResultado = Resultado(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4]))
            self.agregar(nuevoResultado)
        archivo.close()

    def getListaResultados(self):
        return self.__listaResultados
    
    def getCantidad(self):
        return self.__cantidad
    
    def getDenominaciones(self, xfecha, CE):
        recaudacion:int = 0
        for i in range(self.__cantidad):
            if xfecha== self.__listaResultados[i].getFecha():
                recaudacion += self.__listaResultados[i].getInscripcion()*2
                equipoLocal = CE.getNombre(self.__listaResultados[i].getEquipoLocal())
                equipoVisitante = CE.getNombre(self.__listaResultados[i].getEquipoVisitante())
                print(f"Fecha: {xfecha}, Equipo Local: {equipoLocal}, Goles Local: {self.__listaResultados[i].getGolesLocal()}, "
                      f"Equipo Visitante: {equipoVisitante}, Goles Visitante: {self.__listaResultados[i].getGolesVisitante()}\n")
        print(f"Recaudacion total de la fecha {xfecha}: ${recaudacion}")

    def getLocalia(self, xidEquipo, xnombre, CE):
        for i in range(self.__cantidad):
            if xidEquipo == self.__listaResultados[i].getEquipoLocal():
                nombreVisitante= CE.getNombre(self.__listaResultados[i].getEquipoVisitante())
                print(f"Fecha: {self.__listaResultados[i].getFecha()}, Equipo Local: {xnombre}, Goles Local: {self.__listaResultados[i].getGolesLocal()}, "
                      f"Equipo Visitante: {nombreVisitante}, Goles Visitante: {self.__listaResultados[i].getGolesVisitante()}\n")
                
    def cargarResultados(self, CE):
        for i in range(self.__cantidad):
            idLocal = self.__listaResultados[i].getEquipoLocal()
            idVisitante = self.__listaResultados[i].getEquipoVisitante()
            gl= self.__listaResultados[i].getGolesLocal()
            gv= self.__listaResultados[i].getGolesVisitante()
            if gl > gv:
                puntosLocal = 3
                puntosVisitante = 0
            elif gl < gv:
                puntosLocal = 0
                puntosVisitante = 3
            else:
                puntosLocal = 1
                puntosVisitante = 1
            CE.setPuntos(puntosLocal, gl, gv, idLocal)
            CE.setPuntos(puntosVisitante, gv, gl, idVisitante)
    
    def mostrarTablaPosiciones(self, CE):
        pass
            