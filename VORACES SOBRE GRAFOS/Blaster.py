# DIJKSTRA
def calculate_lost(power, distance, lost):
    if distance >= 0 and not distance == float('inf'):
        pw = power - (distance - lost)
        if pw >= 0:
            return pw
    return 0


def _select_min_(distances, visited):
    node = 0
    dist = float('inf')
    for i in range(len(distances)):
        if not visited[i] and distances[i] < dist:
            node = i
            dist = distances[i]
    return node


def piumpium(g, attacker, objetive, power):
    visited = [False] * len(g)
    distances = [float('inf')] * len(g)
    count = 0
    distances[attacker] = 0
    visited[attacker] = True
    path = []

    for start, end, lost in g[attacker]:
        distances[end] = lost

    for i in range(1, len(g)):
        next_node = _select_min_(distances, visited)
        visited[next_node] = True
        path.append(next_node)
        count += distances[next_node]
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances[objetive]


attacker, objetive, power = map(int, input().split())
positions, traject = map(int, input().split())
lost = [int(x) for x in input().split()]
lost.insert(0, 0)

g = [[]]
for i in range(positions):
    g.append([])
for i in range(traject):
    start, end = map(int, input().strip().split())
    g[start].append((start, end, lost[end]))
    g[end].append((end, start, lost[start]))


distance = piumpium(g, attacker, objetive, power)
print(calculate_lost(power, distance, lost[objetive]))
