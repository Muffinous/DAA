def _select_min_(d, visited):
    next = 0
    weight = float('inf')
    for i in range(len(d)):
        if not visited[i] and d[i] < weight:
            next = i
            weight = d[i]
    return next, weight


def prim(graph, start):
    distances = [float('inf')]*len(graph)
    visited = [False]*len(graph)
    visited[start] = True
    count = 0

    for start, end, weight in graph[start]:
        distances[end] = weight

    for i in range(2, len(graph)):
        next, cost = _select_min_(distances, visited)
        if cost < float('inf'):
            visited[next] = True
            count += cost
            for start, end, weight in graph[next]:
                if not visited[end]:
                    distances[end] = min(weight, distances[end])
    return count


nhabilities, npaths = map(int, input().strip().split())
g = [[]]

for i in range(nhabilities):
    g.append([])

for i in range(npaths):
    x, y, cost = map(int, input().strip().split())
    g[x].append((x, y, cost))
    g[y].append((y, x, cost))
cost = prim(g, 1)
print(cost)