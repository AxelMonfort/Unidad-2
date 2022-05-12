from manejadorProyecto import manejador as MP
from manejadorIntegrantes import manejadorIntegrantes as MI
from claseProyecto import Proyecto as proye


if __name__ == '__main__':
    oProyecto = MP()
    oIntegrante = MI(11)
    oProyecto.testManejador()
    oIntegrante.testManejador()
    #print('\n-------PROYECTOS-------')
    #print(oProyecto)
    #print('\n---------INTEGRANTES-----------')
    #print(oIntegrante)

    print('\n-----------INCISO 1------------')
    print('\nEl Proyecto debe tener como mínimo 3 integrantes.')
    proyec = ['2,10E+240','21E442','21E551']
    cont = [0,0,0]
    acum = [0,0,0]
    j, l = 0, 0

    for i in proyec:
        cont[j] = oIntegrante.contar(i)
        if (cont[j] >= 3):
            acum[l] = acum[l] + 10
        else:
            acum[l] = acum[l] - 20
        l = l+1
        j = j+1

    print('\n----------INCISO 2-------------')
    print('El Director del Proyecto debe tener categoría I o II.')
    l = 0
    for i in proyec:
        opcion = oIntegrante.buscar(i)
        if(opcion == 1):
            acum[l] = acum[l] + 10
        else:
            acum[l] = acum[l] - 5
        l = l+1

    print('\n------------INCISO 3------------')
    print('El Codirector del Proyecto debe tener como mínimo categoría III.')
    l = 0
    for i in proyec:
        opcion = oIntegrante.buscar2(i)
        if (opcion == 1):
            acum[l] = acum[l] + 10
        else:
            acum[l] = acum[l] - 5
        l = l + 1

    print('\n---------------INCISO 4-----------')
    print('El Proyecto debe tener un Director o Codirector.')
    l = 0
    for i in proyec:
        opcion = oIntegrante.buscar3(i)
        if (opcion == 1):
            acum[l] = acum[l]
        else:
            acum[l] = acum[l] - 5
        l = l + 1

    print('\nLISTADO DE DATOS CON EL OPERADOR SOBRECARGA ')