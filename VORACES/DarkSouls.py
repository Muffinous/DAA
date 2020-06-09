def solutions(data, sol):
    totalWeight = 0
    for i in range(len(sol)):
        totalWeight += data['defenseValues'][i] * sol[i]
    print("{:.2f}".format(totalWeight))
    objects = []
    for i in range(len(sol)):
        if sol[i]>0:
            objects.append(data.get("items")[i])
    objects.sort()

    for i in range(len(objects)):
        print(objects[i])


def isFeasible(data, bestItem, freeWeight):
    return freeWeight - data['itemWeights'][bestItem] > 0


def getBestItem(data,candidates):
    bestItem = 0
    bestRatio = 0
    for c in candidates:
        r = data['defenseValues'][c]/data['itemWeights'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def selectItem(data):
    n = len(data['items'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    freeWeight = data['maxWeight']
    sol = [0]*n
    isSol = False
    while not isSol and candidates:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        if isFeasible(data, bestItem, freeWeight):
            sol[bestItem] = 1
            freeWeight -= data['itemWeights'][bestItem]
        else:
            sol[bestItem] = freeWeight /data['itemWeights'][bestItem]
            isSol = True
    solutions(data, sol)
    return sol


def calculateWeight(status,weight):
    result = {
        'ligero': ((50 * weight) / 100),
        'medio': ((75*weight)/100),
        'pesado': ((100*weight)/100),
    }[status]
    return result


numberItems = int(input().strip())
weight = int(input().strip())
mode = input().strip()

data = {
    "items": [],
    "itemWeights": [],
    "defenseValues": [],
    "maxWeight": 0}

for j in range(numberItems):
    item, itemWeight, defenseValue = map(str, input().strip().split())
    data['items'].append(item)
    data['itemWeights'].append(int(itemWeight))
    data['defenseValues'].append(int(defenseValue))


sol = calculateWeight(mode,weight)
data['maxWeight'] = sol

# print(numberItems,weight,mode)
# print(data)
# print('peso maximo', sol)

selectItem(data)

