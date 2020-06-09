def isFeasible(last, activity):
    return last <= activity[0]  # if the end is smaller or equal than the new activity's start


def fullactivities(data, nactivities):
    sol = 0  # num of total activities
    last_activity = 0
    for z in range(nactivities):
        if isFeasible(last_activity, data[z]):
            sol += 1
            last_activity = data[z][1]
    return sol


supersol = []
cases = int(input().strip())
for i in range(cases):
    nactivities = int(input().strip())
    activities = [[0, 0] for _ in range(nactivities)]
    schedule = list(map(int, input().strip().split()))
    j = 0
    for y in range(nactivities):
        activities[y][0] = schedule[j]
        activities[y][1] = schedule[j + 1]
        j += 2
    # lambda x: x[1] -> to sort list by the second element of each tuple
    activities.sort(key=lambda x: x[1])
    n = fullactivities(activities, nactivities)
    supersol.append(n)

for i in range(len(supersol)):
    print(supersol[i])
