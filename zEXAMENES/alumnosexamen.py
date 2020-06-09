# COMO EL COLOREADO, BT- HAMILTON


def isFeasible(g, sol, alumn, exam):
    i = 0
    feasible = True
    compis = g['ady'][alumn]
    while feasible and i < len(compis):
        if compis[i] < alumn:
            feasible = sol[compis[i]] != exam
        i += 1
    return feasible


def colocar(graph, exams, sol, alumn):
    if alumn >= graph['n']:
        is_sol = True
    else:
        is_sol = False
        exam = 1
        while not is_sol and exam <= exams:
            if isFeasible(graph, sol, alumn, exam):
                sol[alumn] = exam
                [is_sol, sol] = colocar(graph, exams, sol, alumn + 1)
                if not is_sol:
                    sol[alumn] = 0
            exam += 1
    return is_sol, sol


def initsol(g):
    sol = [0] * g['n']
    return sol


students, relations, exams = map(int, input().strip().split())
graph = [[] for _ in range(students)]

for i in range(relations):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

gr = {
    'n': students,
    'ady': graph
}

sol = initsol(gr)
[exist, g] = colocar(gr, exams, sol, 0)
print(g)
if exist:
    print('OK')
else:
    print('NO HAY SUFICIENTE')