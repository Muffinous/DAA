# no se pueden dividir los objetos, o se coge entero o no.
# Si se pudiese dividir, se haría un voraz.
import copy


def initializeData():
    # = {} <- this is an empty dictionary
    data = {}
    data['N'] = 4
    data['W'] = 8
    data['Weight'] = [2, 3, 4, 5]
    data['Value'] = [3, 5, 6, 10]
    return data


def initializeSolution(datos):
    solution = {}
    solution['Value'] = 0  # this is the value that will be updated
    solution['TWeight'] = 0
    solution['nObjects'] = [0] * datos['N']  # Array where 1 means that the object is in
    return solution


def best(sol1, sol2):
    if sol1['Value'] > sol2['Value']:
        best = copy.deepcopy(sol1)
    else:
        best = copy.deepcopy(sol2)
    return best


def isSolution(solution, data):
    return solution['TWeight'] + min(data['Weight']) > data['W']


def isFeasible(solution, data, i):
    # is <= cause i'm looking if adding THAT object the total weight is 8!!
    # si llega al 8 aun puedo añadir el objeto, no tiene que ser menor!
    return solution['TWeight'] + data['Weight'][i] <= data['W']


def assign(solution, i, data):
    solution['Value'] += data['Value'][i]
    solution['TWeight'] += data['Weight'][i]
    solution['nObjects'][i] += 1
    return solution


def delete(solution, i, data):
    solution['Value'] -= data['Value'][i]
    solution['TWeight'] -= data['Weight'][i]
    solution['nObjects'][i] -= 1
    return solution


def backpackVA(solution, bestSol, data, k):
    if isSolution(solution, data):
        bestSol = best(bestSol, solution)
    else:
        for i in range(k, data['N']):
            if isFeasible(solution, data, i):
                solution = assign(solution, i, data)
                bestSol = backpackVA(solution, bestSol, data, i)
                solution = delete(solution, i, data)
    return bestSol


data = initializeData()
# Represent the solution
solution = initializeSolution(data)
bestSol = initializeSolution(data)
bestSol = backpackVA(solution, bestSol, data, 0)
print(bestSol)