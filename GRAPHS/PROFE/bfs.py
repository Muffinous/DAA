from collections import deque

def bfsAux(g, visited, v):
    q = deque()
    visited[v] = True
    print(v, end=" ")
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                print(adj, end=" ")
                q.append(adj)


def bfs(g):
    n = len(g)
    visited = [False] * n
    for v in range(1,n):
        if not visited[v]:
            bfsAux(g, visited, v)


# En el cero se mete una lista vacia para ignorar la posicion
g = [
    [],
    [2,4,8],
    [1,3,4],
    [2,4,5],
    [1,2,3,7],
    [3,6],
    [5,7],
    [4,6,9],
    [1,9],
    [7,8]
]

bfs(g)