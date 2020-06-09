from collections import deque

def toposortVisit(data, u):
    data["state"][u] = "VISITED"
    data["time"] = data["time"]+1
    data["d"][u] = data["time"]
    for adj in data["g"][u]:
        if data["state"][adj] == "NOT_VISITED":
            data["parent"][adj] = u
            toposortVisit(data, adj)
    data["state"][u] = "FINISH"
    data["time"] = data["time"]+1
    data["f"][u] = data["time"]
    data["list"].appendleft(u)

def toposort(g):
    data = {
        "g": g,
        "state": dict(),
        "parent": dict(),
        "d": dict(),
        "time": 0,
        "f": dict(),
        "list": deque()
    }

    for k in range(1,len(g)):
        data["state"][k] = "NOT_VISITED"
        data["parent"][k] = None
        data["d"][k] = 0
        data["f"][k] = 0
    for k in range(1,len(g)):
        if data["state"][k] == "NOT_VISITED":
            toposortVisit(data, k)

    return data['list']


def transpose(g):
    transposed = []
    n = len(g)
    for v in range(n):
        transposed.append([])

    for v in range(1,n):
        for u in g[v]:
            transposed[u].append(v)

    return transposed


def auxDFS(v, t, visited, output):
    visited[v] = True
    output.append(v)
    for u in t[v]:
        if not visited[u]:
            auxDFS(u, t, visited, output)
    return output


def findSCC(g):
    n = len(g)
    topo = toposort(g)
    t = transpose(g)

    visited = [False] * n
    scc = []
    for v in topo:
        if not visited[v]:
            component = auxDFS(v, t, visited, [])
            scc.append(component)
    return scc



g = [
    [],
    [3,4],
    [1],
    [2],
    [5],
    []
]

g2 = [
    [],
    [2,5],
    [3],
    [4],
    [2],
    [6,7],
    [1],
    []
]

scc = findSCC(g)
print(scc)