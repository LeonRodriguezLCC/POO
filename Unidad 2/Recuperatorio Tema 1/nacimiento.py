class Nacimiento:
    __DNI:int
    __tipo:str
    __fecha:str
    __hora:str
    __peso:float
    __altura:int
    
    def __init__(self, dni, tipo, fecha, hora, peso, altura):
        self.__DNI=dni
        self.__tipo=tipo
        self.__fecha=fecha
        self.__hora=hora
        self.__peso=peso
        self.__altura=altura

    def getDNI(self):
        return self.__DNI
    
    def getTipo(self):
        return self.__tipo
    
    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora

    def getPeso(self):
        return self.__peso  

    def getAltura(self):
        return self.__altura
    
    def __eq__(self, xNacimiento):
        return self.__fecha==xNacimiento.getFecha()
    
    def __str__(self):
        return f"   {self.__peso}       {self.__altura}"