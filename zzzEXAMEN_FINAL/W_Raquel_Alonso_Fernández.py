def isSolution(start, end):
    return start == end


def isFeasible(board, nextpos, turno):
    if board[nextpos[0]][nextpos[1]] == 2:
        return True
    if 0 <= nextpos[0] < len(board) and 0 <= nextpos[1] < len(board[0]):
        odd = turno % 2 == 0  # si es impar
        return not odd and board[nextpos[0]][nextpos[1]] == -1 or board[nextpos[0]][nextpos[1]] == 0 # y no es pared
    return False


def humoramarillo(b, start, end, mov, k, bestsol):
    if isSolution(start, end):
        bestsol = min(bestsol, k)
    else:
        for i in range(len(movs['x'])):
            next_mov = [start[0] + mov['x'][i], start[1] + mov['y'][i]]
            if isFeasible(b, next_mov, k):
                b[next_mov[0]][next_mov[1]] = k
                k += 1
                bestsol = humoramarillo(b, next_mov, end, mov, k, bestsol)
                k -= 1
                b[next_mov[0]][next_mov[1]] = 0
    return bestsol


rows, columns = map(int, input().strip().split())
board = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    board.append(row)

movs = {
    'x': [0, 0, 1, -1],
    'y': [1, -1, 0, 0]
}
start = [0, 0]
end = []
for i in range(rows):
    for j in range(columns):
        if board[i][j] == 2:
            end = [i, j]

bestsol = float('inf')
shortest = humoramarillo(board, start, end, movs, 1, bestsol)
print(shortest)
