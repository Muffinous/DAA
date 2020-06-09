

def getBestItem(data, candidates):
    # Select the best item in terms of
    # ratio profit / weight, better
    # have them sorted
    bestRatio = 0
    bestItem = 0
    for c in candidates:
        r = data['profit'][c] / data['weight'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def isFeasible(data, bestItem, freeWeight):
    return freeWeight - data['weight'][bestItem] > 0


def greedyKnapsack(data):
    n = len(data['profit'])
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
            sol[bestItem] = 1.0
            freeWeight -= data['weight'][bestItem]
        else:
            sol[bestItem] = freeWeight / data['weight'][bestItem]
            isSol = True
    return sol


n = 5
data = {'profit': [20, 30, 66, 40, 60], 'weight': [10, 20, 30, 40, 50], 'maxWeight': 100}
sol = greedyKnapsack(data)
print(sol)


