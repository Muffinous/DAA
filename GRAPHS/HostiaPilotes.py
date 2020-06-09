from collections import deque
# ES UN BFS

def comiendoPilotesAux(g, visited, i):
    q = deque()
    visited[i] = True
    q.append(i)
    while q:
        aux = q.popleft()
        for ady in g[aux]:
            if not visited[ady]:
                visited[ady] = True
                q.append(ady)


def comiendoPilotes(g):
    n = len(g);  # 10
    visited = [False] * n
    cucharadas = 0
    for i in range(n):
        if not visited[i]:
            cucharadas +=1
            comiendoPilotesAux(g,visited,i)
    print(cucharadas)


numPilotes, pilotesSinPatatas = map(int, input().strip().split())
#  print(numPilotes, pilotesSinPatatas)

g = []
#  g = [[1], [0, 5], [4], [9], [2, 9], [1], [], [], [], [3, 4]]

for i in range(numPilotes):
    g.append([])

for i in range(pilotesSinPatatas):
    x, y = map(int, input().strip().split())
    g[x].append(y)
    g[y].append(x)


comiendoPilotes(g)
