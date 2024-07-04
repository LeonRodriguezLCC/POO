class miembro():
    __id:int
    __ApellidoNombre:str
    __email:str
    def __init__(self,iD,Usuario,Email) -> None:
        self.__ApellidoNombre=Usuario
        self.__email=Email
        self.__id=int(iD)

    def getNombre(self):
        return self.__ApellidoNombre
    def getID(self):
        return self.__id
    def getEmail(self):
        return self.__email
    def __str__(self) -> str:
        return ("ID:{:10} Nombre y Apellido:{:10} Email:{:10}".format(self.__id,self.__ApellidoNombre,self.__email))