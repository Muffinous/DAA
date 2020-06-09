
n_activities = int(input().strip())

data = {
    "start": [],
    "end": [],
    "points": []
}

for i in range(n_activities):
    start, end, points = map(int, input().strip().split())
    data['start'].append(start)
    data['end'].append(end)
    data['points'].append(points)

print(data)
