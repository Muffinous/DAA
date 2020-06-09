from random import randint


# Complexity O(V)
def __select_min__(shortest_edges, visit):
    vertex = None
    weight = float('inf')
    for i in range(1, len(shortest_edges)):
        if not visit[i] and shortest_edges[i] < weight:
            vertex = i
            weight = shortest_edges[i]
    return vertex, weight


# Complexity: O(V*E)
def prim(graph):
    # graph nodes go from 1 to N
    initial = randint(1, len(graph))
    visit = [False] * len(graph)
    mst = 0

    visit[initial] = True
    shortest_edges = [float('inf')] * len(graph)
    for start, end, weight in graph[initial]:
        shortest_edges[end] = weight

    for i in range(2, len(graph)):
        next_node, cost = __select_min__(shortest_edges, visit)
        if cost < float('inf'):  # if not unreachable
            visit[next_node] = True
            mst += cost
            for edge in graph[next_node]:
                start, end, weight = edge
                if not visit[end]:
                    shortest_edges[end] = min(shortest_edges[end], weight)

    return mst


# Grafo
# - En el cero metemos una lista vacia para ignorar esa posicion
# - Cada arista tiene (origen, destino, peso)
# grafo no dirigido (diapositiva 8)

g = [
    [],
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 7, 5), (3, 4, 3)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)],
]

print("Minimum spanning tree (cost): ", prim(g))
