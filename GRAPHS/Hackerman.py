count = 0
# ES UN BFS


def reforzarNodosAux(g, visited, i):
    global count
    visited[i] = True
    disc[i] = count
    count = count + 1
    for adj in g[i]:
        if preNum[adj] > i:
            preNum[adj] = i
        if not visited[adj]:
            reforzarNodosAux(g, visited, adj)


def reforzarNodos(g):
    n = len(g)
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            reforzarNodosAux(g, visited, i)


numNodos, conexionesNodos = map(int, input().strip().split())


g = []
coste = 0
disc = [0] * numNodos
preNum = [numNodos] * numNodos
values = []

for i in range(numNodos):
    g.append([])

for i in range(numNodos):
    values.append(int(input().strip()))

for i in range(conexionesNodos):
    x, y = map(int, input().strip().split())
    g[x].append(y)
    g[y].append(x)

print(g)
print(numNodos, conexionesNodos)
print(g)
reforzarNodos(g)

for hijo in range(1, numNodos):
    padre = preNum[hijo]
    if preNum[hijo] >= disc[padre]:
        if padre == 0 and preNum[padre] == 1:
            None
        else:
            coste = coste + values[padre]
            values[padre] = 0
print(coste)