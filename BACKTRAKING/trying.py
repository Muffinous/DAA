

def isSolution(route, d):
    return route[len(route)-1] == 0 and not len(route) - 1 == 0 and len(route) - 1 == d['nplanets']


def isvisited(visited, num):
    for i in range(1, len(visited)):
        if num == visited[i] and not i == len(visited) - 1:
            return True
    return False


def isFeasible(firstplanet, secondplanet, actualroute, num):
    visited_f = isvisited(actualroute, firstplanet[num])
    visited_s = isvisited(actualroute, secondplanet[num])
    return firstplanet[num] == actualroute[len(actualroute)-1] and not visited_f and not visited_s


def solve(data, route, bestsol, visited):
    if isSolution(visited, data):
        bestsol += 1
    else:
        for i in range(data['nconex']):
            if isFeasible(data['planetA'], data['planetB'], visited, i):
                visited.append(data['planetB'][i])
                bestsol = solve(data, route, bestsol, visited)
                visited.pop()
            elif isFeasible(data['planetB'], data['planetA'], visited, i):
                visited.append(data['planetA'][i])
                bestsol = solve(data, route, bestsol, visited)
                visited.pop()
    return bestsol


data = {
    'nplanets': 0,
    'nconex': 0,
    'planetA': [],
    'planetB': []
}

planets, conexions = map(int, input().strip().split())
data['nplanets'] = planets
data['nconex'] = conexions

for i in range(conexions):
    planetA, planetB = map(int, input().strip().split())
    data['planetA'].append(planetA)
    data['planetB'].append(planetB)

visitedPlanets = [0]
route = 0
bestsol = 0
best = solve(data, route, bestsol, visitedPlanets)
print(best)
