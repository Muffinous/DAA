def getbestpenny(allpennies, change, value):
    best = 0
    for i in range(len(allpennies)):
        if allpennies[i] + change <= value:
            best = i
    return best


def solution(c, v):
    return c == v


def isFeasible(change, bestpenny, pennies, value):
    return change + pennies[bestpenny] <= value


def cambioVoraz(value, pennies):
    penny = 0
    change = 0
    candidates = set()
    for i in range(len(pennies)):
        candidates.add(i)
    while candidates and not solution(change, value):
        bestpenny = getbestpenny(pennies, change, value)
        if isFeasible(change, bestpenny, pennies, value):
            change += pennies[bestpenny]
            penny += 1
    return penny


pennies = [0.1, 0.2, 0.3, 0.5, 1, 2]
n = cambioVoraz(5, pennies)
print(n)