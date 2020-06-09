def disparidad(levels):
    dsfgdg = max(abs(levels[0][0] - levels[1][0]), abs(levels[0][0] - levels[2][0]), abs(levels[1][0] - levels[2][0]))
    return dsfgdg


def alladded(added):
    for i in range(len(added)):
        if not added[i]:
            return False
    return True


def isSolution(g, added):
    alladd = alladded(added)
    return g[0][0] != 0 and g[1][0] != 0 and g[2][0] != 0 and alladd


def isFeasible(k, added):
    return added[k] == False


def battleroyale(levels, groups, added, b, k):
    if isSolution(groups, added):
        new = disparidad(groups)
        b = min(b, new)
    else:
        if k < players:
            for j in range(3):
                if isFeasible(k, added):
                    groups[j][0] += levels[k]
                    added[k] = True
                    b = battleroyale(levels, groups, added, b, k + 1)
                    groups[j][0] -= levels[k]
                    added[k] = False
    return b


players = int(input().strip())
levels = list(map(int, input().split()))
g = [[0], [0], [0]]
add = [False] * players
b = float('inf')
print(battleroyale(levels, g, add, b, 0))
