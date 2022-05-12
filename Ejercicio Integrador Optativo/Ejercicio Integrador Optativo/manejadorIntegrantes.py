import csv
from claseIntegrantes import Integrante as inte
import numpy as np

class manejadorIntegrantes:
    __cantidad = 0
    __dimension = 0
    __incremento = 11

    def __init__(self, dimension, incremento=11):
        self.__integrantes = np.empty(dimension, dtype=inte)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ''
        for inte in self.__integrantes:
            s += str(inte) + '\n'
        return s

    def agregar(self, objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__integrantes.resize(self.__dimension)
        self.__integrantes[self.__cantidad] = objeto
        self.__cantidad += 1

    def testManejador(self):
        archi = open('integrantes')
        reader = csv.reader(archi,delimiter = ';')
        for i in reader:
            id = i[0]
            ayn = i[1]
            dni = i[2]
            categoria = i[3]
            rol = i[4]
            objeto = inte(id,ayn,dni,categoria,rol)
            self.agregar(objeto)
        archi.close()

    def contar(self,i):
        cont = 0
        for inte in self.__integrantes:
            if (inte.getId() == i):
                cont = cont + 1
        return cont

    def buscar(self,i):
        for inte in self.__integrantes:
            if (inte.getId() == i):
                if(inte.getRol() == 'director'):
                    if(inte.getCategoria() == 'I' or inte.getCategoria() == 'II'):
                        return 1


    def buscar2(self,i):
        for inte in self.__integrantes:
            if (inte.getId() == i):
                if(inte.getRol() == 'codirector'):
                    if(inte.getCategoria() == 'I' or inte.getCategoria() == 'II' or inte.getCategoria() == 'III'):
                        return 1
        return 0

    def buscar3(self,i):
        for inte in self.__integrantes:
            if (inte.getId() == i):
                if(inte.getRol() == 'director' or inte.getRol() == 'codirector'):
                    return 1
        return 0