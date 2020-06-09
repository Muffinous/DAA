# A FUCKING KRUSKAL, GREEDY VORAZ


def dora(g):
    elements = list(range(len(g)))
    conex_cost = 0
    conex_nodes = len(g)  # number of initial connected components

    edges = []
    for edgeslist in g:
        for start, end, weight in edgeslist:
            if start < end:
                edges.append((weight, start, end))
    edges.sort()
    print(edges)
    i = 0
    while i < len(edges) and conex_nodes > 1:
        weight, start, end = edges[i]
        if elements[start] != elements[end]:
            conex_nodes -= 1
            conex_cost += weight
            __update_elements__(elements, elements[start], elements[end])
        i += 1
    return conex_cost


def __update_elements__(elements, old, new):
    for i in range(len(elements)):
        if elements[i] == old:
            elements[i] = new


g = []
clients, conex = map(int, input().strip().split())
for i in range(clients):
    g.append([])

for i in range(conex):
    clientA, clientB, cost = map(int, input().strip().split())
    g[clientA].append((clientA, clientB, cost))
    g[clientB].append((clientB, clientA, cost))

mycost = dora(g)
print(mycost)