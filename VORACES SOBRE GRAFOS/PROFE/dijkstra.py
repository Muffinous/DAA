def select_min(distances, visit):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visit[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


# Complexity: O(V^2)
def dijkstra(origin, destination, graph):
    # distances from origin to all other
    distances = [float('inf')] * len(graph)
    visit = [False] * len(graph)

    distances[origin] = 0
    visit[origin] = True
    for start, end, weight in graph[origin]:
        distances[end] = weight

    for i in range(2, len(graph)):
        next_node = select_min(distances, visit)
        visit[next_node] = True
        for start, end, weight in graph[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances[destination]


def main():
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

    print(dijkstra(1, 7, g))

    # grafo dirigido (diapositiva 19)
    g2 = [
        [],
        [(1, 2, 5), (1, 4, 3)],
        [(2, 5, 1)],
        [],
        [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
        [(5, 3, 1)]
    ]
    print(dijkstra(1, 3, g2))


if __name__ == "__main__":
    main()
