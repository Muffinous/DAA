# PRIM


def _select_min_(distances, visited):
    # selecciona el nodo que tiene el coste mas chiquitito
    next = None
    weight = float('inf')

    for i in range(len(distances)):
        if not visited[i] and distances[i] < weight:
            next = i
            weight = distances[i]
    return next, weight


def getAllSkills(g, initial):
    visited = [False] * len(g)
    count = 0

    visited[initial] = True
    distances = [float('inf')] * len(g)
    for start, end, weight in g[initial]:
        distances[end] = weight

    for i in range(2, len(g)):
        next_node, cost = _select_min_(distances, visited)
        if cost < float('inf'):
            visited[next_node] = True
            count += cost
            for edge in g[next_node]:
                start, end, weight = edge
                if not visited[end]:
                    distances[end] = min(distances[end], weight)
    return count


skills, paths = map(int, input().strip().split())
g = [[]]

for i in range(skills):
    g.append([])

for j in range(paths):
    x, y, cost = map(int, input().strip().split())
    g[x].append((x, y, cost))
    g[y].append((y, x, cost))

print(getAllSkills(g, 1))
