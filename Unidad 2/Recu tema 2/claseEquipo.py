class Equipo:
    __idEquipo:str
    __denominacion:str
    __presidente:str
    __puntos:int
    __gf:int
    __gc:int
    __dg:int

    def __init__(self, idEquipo, denominacion, presidente, puntos, gf, gc, dg):
        self.__idEquipo = idEquipo
        self.__denominacion = denominacion
        self.__presidente = presidente
        self.__puntos = puntos
        self.__gf = gf
        self.__gc = gc
        self.__dg = dg

    def getIdEquipo(self):
        return self.__idEquipo
    def getDenominacion(self):
        return self.__denominacion
    def getPresidente(self):
        return self.__presidente
    def getPuntos(self):
        return self.__puntos
    def getGF(self):
        return self.__gf
    def getGC(self):
        return self.__gc
    def getDG(self):
        return self.__dg
    def setPuntos(self, puntos):
        self.__puntos = puntos
    def setGF(self, gf):
        self.__gf = gf
    def setGC(self, gc):
        self.__gc = gc
    def setDG(self, dg):
        self.__dg = dg
    
    
    def __gt__(self, otro):
        return self.__puntos > otro.getPuntos() or (self.__puntos == otro.getPuntos() and self.__dg > otro.getDG())
    
    def __str__(self):
        return f"Equipo: {self.__denominacion}, Presidente: {self.__presidente}, Puntos: {self.__puntos}, GF: {self.__gf}, GC: {self.__gc}, DG: {self.__dg}"
        