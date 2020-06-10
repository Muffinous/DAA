import copy


def InicializarDatos():
    datos = {'N': 4,
             'W': 15,
             'valor': [10, 10, 12, 18],
             'peso': [2, 4, 6, 9],
             'v/p': [5., 2.5, 2., 2.]}
    return datos


def GenerarTuplaVacia(datos):
    solucion = {
        'cota': datos['W'] * datos['v/p'][0],
        'tupla': [-1] * datos['N'],
        'tope': 0,
        'valor': 0,
        'peso': 0}
    return solucion


def SolucionMejorInicial(datos):
    solucion = {'tupla': [-1] * datos['N'], 'peso': 0, 'valor': 0}
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


def complecciones(sol, datos):
    # Dos posibilidades (se incluye o no el objeto en la solucion):
    hijo1 = copy.deepcopy(sol)
    hijo2 = copy.deepcopy(sol)
    hijo1 = asignar(hijo1, 0, datos)
    hijo2 = asignar(hijo2, 1, datos)
    return [hijo1, hijo2]


def esFactible(sol, datos):
    return sol['peso'] <= datos['W']


def encolar(q, sol):
    i = 0
    while i < len(q) and sol['cota'] <= q[i]['cota']:
        i += 1
    q = q[:i] + [sol] + q[i:]
    return q


def desencolar(q):
    return [q[0], q[1:]]


def crearColaVacia():
    return []


def esColaVacia(q):
    return q == []


def RamificacionYPoda(datos):
    solMejor = SolucionMejorInicial(datos)  # Algoritmo voraz
    sol = GenerarTuplaVacia(datos)  # Tupla parcial inicialmente vacía
    q = crearColaVacia()
    q = encolar(q, sol)  # se añade la sol inicial
    while not esColaVacia(q):
        [sol, q] = desencolar(q)  # Sol es el nodo de prioridad max
        if esSolucion(sol):
            if sol['valor'] > solMejor['valor']:
                solMejor = sol  # Se actualiza SolMejor
        else:
            if sol['cota'] > solMejor['valor']:  # Criterio de poda
                hijos = complecciones(sol, datos)
                for hijo in hijos:
                    if esFactible(hijo, datos) and sol['cota'] > solMejor['valor']:
                        q = encolar(q, hijo)
    return solMejor


# Pog Ppal:
datos = InicializarDatos()
sol = RamificacionYPoda(datos)
print('La mejor solucion es:', sol)
