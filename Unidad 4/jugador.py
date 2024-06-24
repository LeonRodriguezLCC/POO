class Jugador:
    def __init__(self, nom, puntos, fecha, hora):
        self.__nombre = nom
        self.__puntos = puntos
        self.__fecha = str(fecha)
        self.__hora = str(hora)

    def __str__(self):
        return f"{self.__nombre}".center(25) + f"{self.__puntos}".center(25) + f"{self.__fecha}".center(25) + f"{self.__hora}".center(25)

    def __gt__(self, otro):
        return self.__puntos > otro.getPuntos()

    def getPuntos(self):
        return self.__puntos

    def getDatos(self):
        return [self.__nombre,self.__puntos,self.__fecha,self.__hora]

    def toJSON(self):
        return {
            '__class__': self.__class__.__name__,
            '__atributos__': {
                'nombre': self.__nombre,
                'puntos': self.__puntos,
                'fecha': self.__fecha,
                'hora': self.__hora
            }
        }
