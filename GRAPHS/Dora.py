numCiudades, carreterasEsp = map(int, input().strip().split())

g = []
distance = []

for i in range(numCiudades):
    g.append([])

for i in range(carreterasEsp):
    a, b, dist = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)
    # g[a].append(dist)

print(g)