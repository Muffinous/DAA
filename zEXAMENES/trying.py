# greedy o divide????????????


def mayoriaabs(data):
    sol = 0
    for i in range(len(data)):
        sol += data[i][1]
    return sol


def pacto(d, gobernador, sol):
    mayoria = mayoriaabs(d)
    mindip = len(d) // 2 + 1
    print(mayoria, mindip, d[gobernador])

    if len(sol) < mindip:

    else:
        return sol


politicos = int(input().strip())
d = []
ganador = gobernador = 0
for i in range(politicos):
    name, diputados, perjuicio = map(str, input().strip().split())
    dip = int(diputados)
    per = int(perjuicio)
    d.append((per, dip, name))
d.sort()

for i in range(politicos):
    diputados = d[i][1]
    if diputados > ganador:
        ganador = diputados
        gobernador = i

print(d)
pacto(d, gobernador, sol)
