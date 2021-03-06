def isSolution(start, end, salas_visited):
    return all(salas_visited) and start == end


def isFeasible(b, next, copy):
    if next[0] < len(b) and next[1] < len(b[0]):
        return b[next[0]][next[1]] != 2 and not copy[next[0]][next[1]]
    return False


def best(sol1, sol2):
    if sol1 > sol2:
        best = sol2
    else:
        best = sol1
    return best


def ikea(b, sections, start, end, bestsol, mov, visited, k, copy):
    if isSolution(start, end, salas_visited):
        bestsol = best(bestsol, k)
    else:
        for i in range(len(mov['x'])):
            next_mov = [start[0] + mov['x'][i], start[1] + mov['y'][i]]
            if isFeasible(b, next_mov, copy):
                if not visited[b[next_mov[0]][next_mov[1]]]:
                    visited[b[next_mov[0]][next_mov[1]]] = True
                copy[next_mov[0]][next_mov[1]] = True
                k += 1
                bestsol = ikea(b, sections, next_mov, end, bestsol, mov, visited, k, copy)
                k -= 1
                copy[next_mov[0]][next_mov[1]] = False
    return bestsol


rows, columns, sections = map(int, input().strip().split())
board = []
copy = []
for i in range(rows):
    mat = [False] * columns
    copy.append(mat)

for i in range(rows):
    values = list(map(int, input().strip().split()))
    board.append(values)

start = end = []
for i in range(rows):
    for j in range(columns):
        if board[i][j] == 0:
            start = [i, j]
        elif board[i][j] == 1:
            end = [i, j]


# right, left, down, up
mov = {
    'x': [0, 0, 1, -1],
    'y': [1, -1, 0, 0]
}

seccion = set()
salas_visited = []
for i in range(3):  # inicializo los 3 primeros a False porque las secciones empiezan a partir del 3
    salas_visited.append(True)
for i in range(3, sections + 3):
    seccion.add(i)
    salas_visited.append(False)

bestsol = float('inf')
sol = ikea(board, sections, start, end, bestsol, mov, salas_visited, 1, copy)

print(sol)

'''
6 7 4
2 2 2 2 2 2 2
2 2 1 2 2 0 2
2 6 6 2 3 3 2 
2 6 6 2 3 3 2
2 2 5 5 4 2 2 
2 2 2 2 4 2 2 
'''