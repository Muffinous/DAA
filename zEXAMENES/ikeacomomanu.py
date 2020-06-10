def isSolution(ini, final, salas_visited):
    return ini == final and all(salas_visited)


def isFeasible(b, next):
    if next[0] < len(b) and next[1] < len(b[0]):
        return b[next[0]][next[1]] != 2 and not b[next[0]][next[1]] == 'x'
    return False


def ikea(b, start, end, best, mov, sala_visited, k, lastroom):
    if isSolution(start, end, salas_visited):
        best = min(best, k)
    else:
        for i in range(len(mov['x'])):
            next_mov = [start[0] + mov['x'][i], start[1] + mov['y'][i]]
            if isFeasible(b, next_mov):
                lastroom.append(b[next_mov[0]][next_mov[1]])
                if not sala_visited[b[next_mov[0]][next_mov[1]]]:
                    sala_visited[b[next_mov[0]][next_mov[1]]] = True
                b[next_mov[0]][next_mov[1]] = 'x'
                k += 1
                best = ikea(b, next_mov, end, best, mov, sala_visited, k, lastroom)
                k -= 1
                b[next_mov[0]][next_mov[1]] = lastroom[len(lastroom) - 1]
    return best


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
sol = ikea(board, start, end, bestsol, mov, salas_visited, 1, [])

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
