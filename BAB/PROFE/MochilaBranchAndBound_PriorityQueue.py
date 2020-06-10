import copy
from queue import PriorityQueue


def InicializarDatos():
    datos = {}
    datos['N'] = 4
    datos['W'] = 15
    datos['valor'] = [10, 10, 12, 18]
    datos['peso'] = [2, 4, 6, 9]
    datos['v/p'] = [5., 2.5, 2., 2.]
    return datos


def GenerarTuplaVacia(datos):
    solucion = {}
    solucion['cota'] = datos['W'] * datos['v/p'][0]
    solucion['tupla'] = [-1] * datos['N']
    solucion['tope'] = 0
    solucion['valor'] = 0
    solucion['peso'] = 0
    return solucion


def SolucionMejorInicial(datos):
    solucion = {}
    solucion['tupla'] = [0] * datos['N']
    solucion['peso'] = 0
    solucion['valor'] = 0
    i = 0
    while i < datos['N'] and solucion['peso'] < datos['W']:
        if solucion['peso'] + datos['peso'][i] <= datos['W']:
            solucion['peso'] += datos['peso'][i]
            solucion['valor'] += datos['valor'][i]
            solucion['tupla'][i] = 1
        i += 1
    solucion['cota'] = solucion['valor']
    solucion['tope'] = datos['N']
    return solucion


def esSolucion(sol):
    return sol['tope'] == len(sol['tupla'])


def asignar(sol, valor, datos):
    sol['tupla'][sol['tope']] = valor
    sol['valor'] += valor * datos['valor'][sol['tope']]
    sol['peso'] += valor * datos['peso'][sol['tope']]
    if sol['tope'] == datos['N'] - 1:
        sol['cota'] = sol['valor']
    else:
        sol['cota'] = sol['valor'] + datos['v/p'][sol['tope'] + 1] * (datos['W'] - sol['peso'])
    sol['tope'] += 1
    return sol


def complecciones2(sol, datos):
    # Dos posibilidades (se incluye o no el objeto en la solucion):
    hijo1 = copy.deepcopy(sol)
    hijo2 = copy.deepcopy(sol)
    hijo1 = asignar(hijo1, 0, datos)
    hijo2 = asignar(hijo2, 1, datos)
    return [hijo1, hijo2]


def complecciones(sol, datos):
    # Dos posibilidades (se incluye o no el objeto en la solucion):
    hijos = []
    for i in range(2):
        h = copy.deepcopy(sol)
        asignar(h, i, datos)
        hijos.append(h)
    return hijos


def esFactible(sol, datos):
    return sol['peso'] <= datos['W']


def RamificacionYPoda(datos):
    solMejor = SolucionMejorInicial(datos)  # Algoritmo voraz
    sol = GenerarTuplaVacia(datos)  # Tupla parcial inicialmente vacía

    # PriorityQueue SIEMPRE (1) ordena de menor a mayor en (2) orden lexicografico. (No permite usar un comparador)
    # - Usaremos una prioridad negativa para ordenar de mayor a menor.
    # - Usaremos un identificador para resolver empates, de lo contrario intentaría resolver el
    # empate comparando los diccionarios y el programa fallaría porque no son tipos de datos con
    # un criterio de comparación definido.

    q = PriorityQueue()
    identificador = 0
    q.put((-sol['cota'], identificador, sol))
    identificador += 1

    while not q.empty():
        priority, idsol, sol = q.get()  # Sol es el nodo de prioridad max
        if esSolucion(sol):
            if sol['valor'] > solMejor['valor']:
                solMejor = sol  # Se actualiza SolMejor
        elif sol['cota'] > solMejor['valor']:  # Criterio de poda
            hijos = complecciones(sol, datos)
            for hijo in hijos:
                if esFactible(hijo, datos) and sol['cota'] > solMejor['valor']:
                    q.put((-hijo['cota'], identificador, hijo))
                    identificador += 1
    print("Nodos explorados:", identificador)
    return solMejor


def main():
    datos = InicializarDatos()
    sol = RamificacionYPoda(datos)
    print('La mejor solucion es:', sol)


main()

# La mejor solucion es: {'cota': 38, 'tupla': [1, 1, 0, 1], 'tope': 4, 'valor': 38, 'peso': 15}
#
# Process finished with exit code 0
