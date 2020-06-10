# BFS
# numero de estudiantes, numero de relaciones entre ellos, numero de modelos


from collections import deque


def bfsAux(g, visited, v, conjuntos):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
            else:
                if conjuntos[aux] == conjuntos[adj]:
                    conjuntos[aux] += 1
    return max(conjuntos) + 1


def Colocacion(g, modelos):
    tam = len(g)
    solucion = True
    conjuntos = [0] * tam
    visitados = [False] * tam
    for i in range(tam):
        cont = bfsAux(g, visitados, i, conjuntos)
    if cont > modelos:
        solucion = False
    return solucion


N, M, C = map(int, input().strip().split())
g = []
for i in range(N):
    g.append([])
for i in range(M):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

solucion = Colocacion(g, C)
if solucion:
    print('OK')
else:
    print('NO HAY SUFICIENTE')