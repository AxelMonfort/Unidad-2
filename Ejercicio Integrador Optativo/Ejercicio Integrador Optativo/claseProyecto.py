class Proyecto:
    def __init__(self,idProyecto,titulo,palabrasClaves):
        self.__idProyecto = idProyecto
        self.__titulo = titulo
        self.__palabrasClaves = palabrasClaves
        self.__puntos = 0

    def __str__(self):
        return 'ID: %s Titulo: %s Palabras: %s Puntos: ' % (self.__idProyecto,self.__titulo,self.__palabrasClaves)

    def acumularPuntos(self,puntos):
        self.__puntos = puntos

    def getId(self):
        return self.__idProyecto