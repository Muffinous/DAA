# voraz como la mochila
# 5
# 228 933
# 933 820
# 810 493
# 329 149
# 697 737
# 626


def print_sol(d, sol, ord):
    print(*ord, sep=' ')
    total = 0
    for i in range(len(sol)):
        if sol[i] != 0:
            total += d['points'][i] * sol[i]
    total = (int(total * 100)) / 100.0
    print(total)


def getbestitem(data, candidates):
    best_order = 0
    best_ratio = 0
    for c in candidates:
       ratio = data['points'][c] / data['time'][c]
       if ratio > best_ratio:
           best_order = c
           best_ratio = ratio
    return best_order


def isFeasible(d, best):
    return d['maxtime'] - d['time'][best] >= 0


def overcook(data):
    candidates = set()
    for i in range(data['norders']):
        candidates.add(i)
    is_sol = False
    sol = [0] * data['norders']
    order = []
    while candidates and not is_sol:
        bestitem = getbestitem(data, candidates)
        candidates.remove(bestitem)
        if isFeasible(data, bestitem):
            sol[bestitem] = 1
            order.append(bestitem + 1)
            data['maxtime'] -= data['time'][bestitem]
        else:
            sol[bestitem] = data['maxtime'] / data['time'][bestitem]
            is_sol = True
            order.append(bestitem + 1)
    return sol, order


data = {
    'norders': 0,
    'points': [],
    'time': [],
    'maxtime': 0
}

orders = int(input().strip())
data['norders'] = orders
for i in range(orders):
    p, t = map(int, input().strip().split())
    data['points'].append(p)
    data['time'].append(t)

m = int(input().strip())
data['maxtime'] = m
[sol, order] = overcook(data)
print_sol(data, sol, order)
