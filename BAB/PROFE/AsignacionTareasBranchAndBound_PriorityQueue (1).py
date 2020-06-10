import numpy as np
from queue import PriorityQueue
import copy


def inicializarDatos():
    datos = np.array([[11, 12, 18, 40], [14, 15, 13, 22], [11, 17, 19, 23], [17, 14, 20, 28]])
    return datos

def SolucionMejorInicial(datos):
    solucion = {}
    n = np.size(datos, 0)
    solucion['tupla'] = [0] * n
    solucion['tope'] = n
    solucion['coste'] = 0
    for i in range(n):
        solucion['tupla'][i] = i
        solucion['coste'] += datos[i, i]
    solucion['cota'] = solucion['coste']
    return solucion


def GenerarTuplaVacia(datos):
    solucion = {}
    solucion['tupla'] = [-1] * np.size(datos, 0)
    solucion['tope'] = 0
    solucion['coste'] = 0
    solucion['cota'] = 0
    for i in range(np.size(datos, 0)):
        solucion['cota'] += np.min(datos[i, :])
    return solucion


def esSolucion(sol):
    return sol['tope'] == len(sol['tupla'])


def esta(tarea, sol):
    return tarea in sol['tupla'][0:sol['tope']]


def asignar(sol, valor, datos):
    sol['tupla'][sol['tope']] = valor
    sol['coste'] += datos[sol['tope'], valor]
    sol['tope'] += 1
    sol['cota'] = sol['coste']
    for i in range(sol['tope'], np.size(datos, 0)):
        valormin = np.inf
        for j in range(np.size(datos, 1)):
            if not esta(j, sol) and datos[i, j] < valormin:
                valormin = datos[i, j]
        sol['cota'] += valormin
    return sol


def buscaTareaRestante(sol):
    encontrado = False
    i = -1
    while not encontrado and i < len(sol['tupla']):
        i += 1
        encontrado = i not in sol['tupla'][:sol['tope']]
    return i


def compleccionesFactibles(sol, datos):
    listaHijos = []
    for tarea in range(np.size(datos, 1)):
        hijo = copy.deepcopy(sol)
        if not esta(tarea, sol):  # Solo generamos soluciones factibles
            hijo = asignar(hijo, tarea, datos)
            if hijo['tope'] == len(hijo['tupla']) - 1:
                tareaRestante = buscaTareaRestante(hijo)
                hijo = asignar(hijo, tareaRestante, datos)
            listaHijos.append(hijo)
    return listaHijos


def RamificacionYPoda(datos):
    solMejor = SolucionMejorInicial(datos)
    sol = GenerarTuplaVacia(datos)  # Tupla parcial, inicialmente vacia
    identificador = 0 # id para cada nodo explorado, sirve para romper empates

    q = PriorityQueue()
    q.put((-sol['cota'], identificador, sol))
    identificador += 1
    while not q.empty():
        prioridad, idsol, sol = q.get()
        if sol['cota'] < solMejor['coste']:  # Criterio de poda
            hijos = compleccionesFactibles(sol, datos)
            for hijo in hijos:
                if esSolucion(hijo):
                    if hijo['coste'] < solMejor['coste']:
                        solMejor = hijo
                elif hijo['cota'] < solMejor['coste']:
                    q.put((-sol['cota'], identificador, hijo))
                    identificador += 1
    print("Nodos explorados:", identificador)
    return solMejor


# Prog Ppal:
datos = inicializarDatos()
solucion = RamificacionYPoda(datos)
print('La mejor solucion es:', solucion)

"""
La mejor solucion es: {'tupla': [0, 2, 3, 1], 'tope': 4, 'coste': 61, 'cota': 61}

Process finished with exit code 0
"""
