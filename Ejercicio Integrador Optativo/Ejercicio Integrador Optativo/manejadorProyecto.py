import csv
from claseProyecto import Proyecto as pro

class manejador:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for pro in self.__lista:
            s += str(pro) + '\n'
        return s

    def agregar(self,objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        with open("proyectos.csv") as file:
            reader = csv.reader(file, delimiter=";", skipinitialspace=True)
            for row in reader:
                id = row[0]
                titulo = row[1]
                palabras = row[2]
                unProyecto = pro(id, titulo, palabras)
                self.agregar(unProyecto)

    def puntos(self,valor):
        for pro in self.__lista:
            print(valor)
            pro.acumularPuntos(valor)