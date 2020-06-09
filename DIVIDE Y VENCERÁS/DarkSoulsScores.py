def print_sol(list, enemies):
    for i in range(len(list)):
        value = list[i]
        count = 0
        for j in range(value + 1):
            count += enemies[j]
        print(value + 1, count)


def knights(data, low, high, enemieslvls, knightlvl, l):
    if high + 1 < len(enemieslvls) and high - 1 >= 0:
        if enemieslvls[high - 1] < data['knight_levels'][knightlvl] < enemieslvls[high + 1]:
            l.append(high)
            return
    if low > high:
        l.append(high)
        return

    mid = (low + high) // 2
    if enemieslvls[mid] == data['knight_levels'][knightlvl]:
        l.append(mid)
        return
    elif data['knight_levels'][knightlvl] < enemieslvls[mid]:
        knights(data, low, mid - 1, enemieslvls, knightlvl, l)
    elif data['knight_levels'][knightlvl] > enemieslvls[mid]:
        knights(data, mid + 1, high, enemieslvls,  knightlvl, l)


def coward(data, l):
    for i in range(len(data['knight_levels'])):
        knights(data, 0, data['enemies'] - 1, data['enemies_levels'], i, l)
    print_sol(l, data['enemies_levels'])


data = {
    'enemies': 0,
    'enemies_levels':  [],
    'tries': 0,
    'knight_levels': []
}

enemies = int(input().strip())
data['enemies'] = enemies
levels = list(map(int, input().strip().split()))
data['enemies_levels'] = levels
tries = int(input().strip())
data['tries'] = tries
for i in range(tries):
    lvl = int(input().strip())
    data['knight_levels'].append(lvl)
l = []
coward(data, l)
