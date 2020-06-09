from math import ceil


def attackreceived(data, nfight, candidates):
    sol = 0
    for c in candidates:
        if data['enemyLF'][nfight][c] > 0:
            sol += data['enemyAT'][nfight][c]
    return sol


def getBestItem(data, nfight, candidates):
    bestItem = 0
    bestRatio = 0
    for c in candidates:
        r = data['enemyAT'][nfight][c] / ceil(data['enemyLF'][nfight][c] / data['attack'][nfight])
        if r > bestRatio:  # here i check the value of the attacks
            bestRatio = r
            bestItem = c
    return bestItem


def isFeasible(data, bestItem, nfight):
    return data['enemyLF'][nfight][bestItem] > 0


def solution(damage):
    n = len(damage)
    for i in range(n):
        print(damage[i])


def fight(data, damage):
    nfight = data['combates']
    for i in range(nfight):
        n = len(data['enemyAT'][i])
        candidates = set()
        for j in range(n):
            candidates.add(j)
        damage[i] = attackreceived(data, i, candidates)
        while candidates:
            bestItem = getBestItem(data, i, candidates)
            if isFeasible(data, bestItem, i):
                data['enemyLF'][i][bestItem] = data['enemyLF'][i][bestItem] - data['attack'][i]
                if data['enemyLF'][i][bestItem] <= 0:
                    data['enemyLF'][i][bestItem] = 0
                    candidates.remove(bestItem)
                damage[i] += attackreceived(data, i, candidates)
    solution(damage)
    return damage


data = {
    "combates": 0,
    "attack": [],
    "enemies": [],
    "enemyAT": [],
    "enemyLF": [],
}

comb = int(input().strip())
data['combates'] = comb

for i in range(comb):
    ataque = int(input().strip())
    data['attack'].append(ataque)
    enemies = int(input().strip())
    data['enemies'].append(enemies)

    enemyAttack = str(input().strip())
    number = [int(x) for x in enemyAttack.split(" ")]
    data['enemyAT'].append(number)

    enemyLife = str(input().strip())
    life = [int(x) for x in enemyLife.split(" ")]
    data['enemyLF'].append(life)

# print(data)


damage = []
for i in range(comb):
    damage.append([])

fight(data, damage)
