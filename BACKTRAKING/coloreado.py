def initgraph():
    graph = {
        'n': 5,
        'ady': [[1, 2, 3, 4], [0], [0, 3], [0, 2, 4], [0, 3]]
    }
    return graph


def initsol(g):
    sol = [0]*g['n']
    return sol


def esFactible(g, solution, node, color):
    factible = True
    adyNode = g['ady'][node]
    i = 0
    while factible and i < len(adyNode):
        if adyNode[i] < node:  # para mirar solamente los anteriores a ese nodo
            factible = solution[adyNode[i]] != color
        i += 1
    return factible


def colorear(g, colors, solution, node):
    if node >= g['n']:
        isSol = True
    else:
        isSol = False
        color = 1  # varía de 1 a m
        while not isSol and color <= m:
            if esFactible(g, solution, node, color):
                solution[node] = color
                [sol, isSol] = colorear(g, colors, solution, color + 1)
                if not isSol:
                    sol[node] = 0
            color += 1
    return solution, isSol


graph = initgraph()
sol = initsol(graph)
# dato del problema m = 3 colores
m = 2
start = 0  # empezamos coloreando el nodo 0
[sol, esSol] = colorear(graph, m, sol, start)
print(sol)
