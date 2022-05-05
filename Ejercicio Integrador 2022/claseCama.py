class Cama:
    def __init__(self,idCama,habitacion,estado,nombre,apellido,diagnostico,fechaInternacion,fechaAlta):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__diagnostico = diagnostico
        self.__fechaInternacion = fechaInternacion
        self.__fechaAlta = fechaAlta

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.__idCama,self.__habitacion,self.__estado,self.__nombre,self.__apellido,self.__diagnostico,self.__fechaInternacion,self.__fechaAlta)

    def getId(self):
        return self.__idCama
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getHabitacion(self):
        return self.__habitacion
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaInternacion(self):
        return self.__fechaInternacion
    def getFechaAlta(self):
        return self.__fechaAlta