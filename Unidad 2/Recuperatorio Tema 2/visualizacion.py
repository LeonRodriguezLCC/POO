class visualizacion():
    __IdM:int
    __IdP:str
    __fecha:str
    __hora:str
    __duracion:int
    def __init__(self,M,P,fecha,hora,duracion) -> None:
        self.__IdM=int(M)
        self.__IdP=P
        self.__duracion=int(duracion)
        self.__fecha=fecha
        self.__hora=hora
    def getIDM(self):
        return self.__IdM
    def getIDP(self):
        return self.__IdP
    def getFecha(self):
        return self.__fecha
    def getHora(self):
        return self.__hora
    def getDuracion(self):
        return self.__duracion
    def __eq__(self, other) -> bool:
        n=False
        if self.__IdM ==other.getIDM() and self.__fecha==other.getFecha() and self.__hora==other.getHora():
            n=True
        return n
        
    def __str__(self) -> str:
        return ("ID Miembro:{:10} ID Pelicula:{:10} Fecha:{:10} Hora:{:10} Duracion:{:10}".format(self.__IdM,self.__IdP,self.__fecha,self.__hora,self.__duracion))