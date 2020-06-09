import copy


def initData():
    # dictionary
    data = {
        'N': 4,
        'W': 8,
        'Weights': [2, 3, 4, 5],
        'Values': [3, 5, 6, 10]
    }
    return data


def initSol(data):
    # dictionary
    solution = {
        'Weight': 0,  # total weight occupied
        'Value': 0,  # total value of my items
        'nObjects': [0] * data['N']
    }
    return solution


def isFeasible(data, sol, i):
    return sol['Weight'] + data['Weights'][i] <= data['W']


def isSolution(sol, dat):                                   # si le sumo el menor peso y me paso ya no puedo hacer más,
    return sol['Weight'] + min(dat['Weights']) > dat['W']   # es una solución


def best(sol1, sol2):
    if sol1['Value'] > sol2['Value']:
        best = copy.deepcopy(sol1)
    else:
        best = copy.deepcopy(sol2)  # importantísimo, no se puede hacer sin este copy. Sino la bestsol se borra!!!!
    return best


def assign(solution, data, obj):
    solution['Weight'] += data['Weights'][obj]
    solution['Value'] += data['Values'][obj]
    solution['nObjects'][obj] += 1
    return solution


def remove(solution, data, obj):
    solution['Weight'] -= data['Weights'][obj]
    solution['Value'] -= data['Values'][obj]
    solution['nObjects'][obj] -= 1
    return solution


def solve(solution, data, bestsol, k):
    if isSolution(solution, data):
        bestsol = best(solution, bestsol)
    else:
        for i in range(k, data['N']):
            if isFeasible(data, solution, i):
                solution = assign(solution, data, i)
                bestsol = solve(solution, data, bestsol, i)
                solution = remove(solution, data, i)
    return bestsol


dat = initData()
best_sol = initSol(dat)
sol = initSol(dat)
best_sol = solve(sol, dat, best_sol, 0)
print(best_sol)
