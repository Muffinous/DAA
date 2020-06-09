from random import randint


def read_graph():
    """
    Lectura de un grafo para la entrada del juez.
    :return: grafo como lista de adyacencia
    """
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n)]

    for i in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    return graph


def test_graph():
    """
    (0)---(1)---(2)
      \  /  \  /
      (3)---(4)
    """
    v = 5
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
    graph = [[] for _ in range(v)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def hamiltonian_cycles(current, graph, visited, solution):
    for adjacent in graph[current]:
        if adjacent not in visited:  # esFactible
            visited.add(adjacent)
            solution.append(adjacent)
            if len(solution) == len(graph):  # esCasoBase
                if 0 in graph[adjacent]:  # esSolucion
                    print(solution)
            else:
                hamiltonian_cycles(adjacent, graph, visited, solution)
            solution.pop()
            visited.remove(adjacent)


graph = read_graph()  # read from standart input
# graph = test_graph()
hamiltonian_cycles(0, graph, {0}, [0])

"""
Entrada 1 (triangulo)
3
3
0 1
1 2
0 0
# Salida esperada: 2

Entrada 2 (sobre)
5
8
0 1
0 2
1 2
1 3
1 4
2 3
2 4
3 4
> Salida esperada: 4


"""
