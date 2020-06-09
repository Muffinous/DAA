# greedy o divide????????????
def getgobernador(data):
    ganador = gobernador = 0
    for i in range(data['npoliticos']):
        diputado = data['diputados'][i]
        if diputado > ganador:
            ganador = diputado
            gobernador = i
    return gobernador


def printSolution(data, sol, gobernador):
    print(data['name'][gobernador])
    sol[gobernador] = 0
    diputadost = []
    for i in range(len(sol)):
        if sol[i] > 0:
            diputadost.append(data['name'][i])
    diputadost.sort()

    for i in range(len(diputadost)):
        print(diputadost[i])


def mayoriaabs(data):
    sol = 0
    for i in range(data['npoliticos']):
        sol += data['diputados'][i]
    return sol


def getbestitem(data, cand):
    bestRatio = 0
    bestItem = 0
    for c in cand:
        r = data['diputados'][c] / data['perjuicio'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def isFeasible(data, bestitem, total, mayoria):
    total += data['diputados'][bestitem]
    if total <= mayoria:
        return True
    else:
        return False


def pacto(d, gob, sol):
    mindip = len(d) // 2 + 1
    candidates = set()
    for i in range(data['npoliticos']):
        candidates.add(i)
    candidates.remove(gobernador)
    is_sol = False
    totaldip = d['diputados'][gob]
    while not is_sol and candidates and mindip <= len(candidates) and d['mayoria'] >= totaldip:
        bestitem = getbestitem(d, candidates)
        candidates.remove(bestitem)
        if isFeasible(data, bestitem, totaldip, d['mayoria']):
            sol[bestitem] = 1
            totaldip += d['diputados'][bestitem]
        else:
            sol[bestitem] = (data['mayoria'] - totaldip) / d['diputados'][bestitem]
    return sol


data = {
    'npoliticos': 0,
    'name': [],
    'diputados': [],
    'perjuicio': [],
    'mayoria': 0
}

politicos = int(input().strip())
data['npoliticos'] = politicos

for i in range(politicos):
    name, diputados, perjuicio = map(str, input().strip().split())
    dip = int(diputados)
    per = int(perjuicio)
    data['name'].append(name)
    data['diputados'].append(dip)
    data['perjuicio'].append(per)
data['mayoria'] = mayoriaabs(data) // 2 + 1

gobernador = getgobernador(data)  # veo quien es el que más diputados tiene

sol = [0]*data['npoliticos']
sol[gobernador] = 1

sol = pacto(data, gobernador, sol)
printSolution(data, sol, gobernador)
