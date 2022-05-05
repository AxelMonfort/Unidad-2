class Medicamento:
    def __init__(self,idCama,idMedicamento,nombre,monodroga,presentacion,cantAplicada,precioTotal):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombre = nombre
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantAplicada = cantAplicada
        self.__precioTotal = precioTotal

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.__idCama,self.__idMedicamento,self.__nombre,self.__monodroga,self.__presentacion,self.__cantAplicada,self.__precioTotal)

    def getId(self):
        return self.__idCama
    def getNombre(self):
        return self.__nombre
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantAplicada(self):
        return self.__cantAplicada
    def getPrecio(self):
        return self.__precioTotal