class Resultado:
    __fecha: str
    __equipoLocal: str
    __golesLocal: int
    __equipoVisitante: str
    __golesVisitante: int
    __inscripcion=45000

    def __init__(self, fecha, equipoLocal, golesLocal, equipoVisitante, golesVisitante):
        self.__fecha = fecha
        self.__equipoLocal = equipoLocal
        self.__golesLocal = golesLocal
        self.__equipoVisitante = equipoVisitante
        self.__golesVisitante = golesVisitante
    
    def getFecha(self):
        return self.__fecha
    def getEquipoLocal(self):
        return self.__equipoLocal
    def getGolesLocal(self):
        return self.__golesLocal
    def getEquipoVisitante(self):
        return self.__equipoVisitante
    def getGolesVisitante(self):
        return self.__golesVisitante
    def getInscripcion(self):
        return self.__inscripcion
    
