# Complexity: O(V*E)
def kruskal(graph):
    # component ID where each node belongs to
    components = list(range(len(graph)))  # [0, 1, 2, 3, ..., N]
    count = len(graph) - 1  # number of initial connected components
    mst = 0

    # add all edges
    list_edges = []
    for edgeList in graph:
        for start, end, weight in edgeList:
            if start < end:  # avoid back edges
                list_edges.append((weight, start, end))
    list_edges.sort()  # sorted by order: weight -> start -> end

    i = 0
    while len(list_edges) > i and count > 1:
        weight, start, end = list_edges[i]
        if components[start] != components[end]:
            count -= 1
            mst += weight
            __update_components__(components, components[start], components[end])

        i += 1
    return mst


# Complexity: O(E)
def __update_components__(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


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

print("Minimum spanning tree (cost): ", kruskal(g))
