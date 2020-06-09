

def dfsRec(g, visited, v):
    visited[v] = True
    print(v,end=" ")
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g, visited, adj)


def dfs(g):
    n = len(g)
    visited = [False] * n
    for v in range(1,n):
        if not visited[v]:
            dfsRec(g, visited, v)


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

dfs(g)
