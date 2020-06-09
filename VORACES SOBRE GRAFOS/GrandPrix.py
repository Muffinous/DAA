# DIJKSTRA


def _select_min_(distances, visited):
    next = 0
    min_dist = float('inf')
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next = i
    return next


def run(g, origin):
    visited = [False] * len(g)
    distances = [float('inf')] * len(g)

    distances[origin] = 0
    visited[origin] = True
    for start, end, weight in g[origin]:
        distances[end] = weight

    for i in range(1, len(g)):
        next_node = _select_min_(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)
    return distances


rooms, doors, time = map(int, input().strip().split())
g = []

for i in range(rooms):
    g.append([])

for j in range(doors):
    x, y, distance = map(int, input().strip().split())
    g[x].append((x, y, distance))
    g[y].append((y, x, distance))

dist = 0
distances = run(g, 0)
for i in range(len(distances)):
    dist += distances[i]


if dist <= time:
    print(dist)
else:
    print("Somos un fraude")