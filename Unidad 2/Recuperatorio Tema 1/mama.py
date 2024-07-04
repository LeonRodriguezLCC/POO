class Mama:
    __DNI:int
    __edad:int
    __ayn:str
    def __init__(self, dni, edad, ayn):
        self.__DNI=dni
        self.__edad=edad
        self.__ayn=ayn
    def getDNI(self):
        return self.__DNI
    
    def getEdad(self):
        return self.__edad
    
    def getAyn(self):
        return self.__ayn
    
    def __str__(self):
        return f"Apellido y nombre: {self.__ayn}\nEdad: {self.__edad}\n"