import csv
from manejadorCama import manejadorCama
from claseMedicamento import Medicamento as medi

class manejadorMedicamento:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for Medicamento in self.__lista:
            s += str(Medicamento) + '\n'
        return s

    def agregar(self,objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        archi = open('Medicamentos')
        reader = csv.reader(archi,delimiter = ';')
        for i in reader:
            idCama = i[0]
            idMedi = i[1]
            nombre = i[2]
            monodroga = i[3]
            presentacion = i[4]
            cant = int(i[5])
            precio = int(i[6])
            objeto = medi(idCama,idMedi,nombre,monodroga,presentacion,cant,precio)
            self.agregar(objeto)
        archi.close()

    def obtener(self,id):
        total = 0
        for medi in self.__lista:
            if medi.getId() == id:
                print('\n{}/{}    {}      {}      {}'.format(medi.getNombre(),medi.getMonodroga(),medi.getPresentacion(),medi.getCantAplicada(),medi.getPrecio()))
                total += medi.getCantAplicada() * medi.getPrecio()
        return total