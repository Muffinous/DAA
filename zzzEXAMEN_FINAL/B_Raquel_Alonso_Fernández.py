def isFeasible(new, time):
    return time <= new[1]  # if the end is smaller or equal than the new activity's start


def calc_actividades(data, nactivities):
    sol = 0
    time = data[0][1] + data[0][2]
    for i in range(nactivities):
        if isFeasible(data[i], time):
            sol += 1  # num of total activities
            time = data[i][1] + data[i][2]
    return sol


nactivities = int(input().strip())

schedule = [[0, 0, 0] for _ in range(nactivities)]
j = 0
for y in range(nactivities):
    tarea, start, end = map(str, input().strip().split())
    schedule[y][0] = tarea
    schedule[y][1] = int(start)
    schedule[y][2] = int(end)

schedule.sort(key=lambda x: x[1])
print(schedule)
calc_actividades(schedule, nactivities)
