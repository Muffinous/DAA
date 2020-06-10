



def isFeasible(act, h):
    return act[0] >= h


def greedySchedule(data):
    data.sort(key=lambda x: x[1])
    lastHour = 0
    counterStrike = 0
    for activity in data:
        if isFeasible(activity, lastHour):
            counterStrike += 1
            lastHour = activity[1]
    print(counterStrike)

t = int(input().strip())

for i in range(t):
    actividades = []
    n = int(input().strip())
    pre = list(map(int, input().strip().split()))
    for h in range(n):
        actividades.append([pre[2*h], pre[2*h + 1]])
    greedySchedule(actividades)
