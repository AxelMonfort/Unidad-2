class Integrante:
    def __init__(self,idProyecto,ayn,dni,categoria,rol):
        self.__idProyecto = idProyecto
        self.__ayn = ayn
        self.__dni = dni
        self.__categoria = categoria
        self.__rol = rol

    def __str__(self):
        return '%s %s %s %s %s' % (self.__idProyecto,self.__ayn,self.__dni,self.__categoria,self.__rol)

    def getId(self):
        return self.__idProyecto
    def getCategoria(self):
        return self.__categoria
    def getRol(self):
        return self.__rol