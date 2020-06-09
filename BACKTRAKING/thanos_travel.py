def trip(current, graph, visited, sol, total):
    for ady in graph[current]:
        if ady not in visited:  # factible
            visited.add(ady)
            sol.append(ady)
            if len(sol) == len(graph):
                if 0 in graph[ady]:
                    total += 1
            else:
                total = trip(ady, graph, visited, sol, total)
            sol.pop()
            visited.remove(ady)
    return total


planets, conexions = map(int, input().strip().split())

graph = [[] for _ in range(planets)]

for i in range(conexions):
    planetA, planetB = map(int, input().strip().split())
    graph[planetA].append(planetB)
    graph[planetB].append(planetA)

print(graph)
total = trip(0, graph, {0}, [0], 0)
print(total)

