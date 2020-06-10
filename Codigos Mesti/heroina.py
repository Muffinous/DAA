

def initializeBoard(horse_pos, final_pos):
    board = [[0] * 6 for x in range(6)]
    for i in range(6):
        for j in range(6):
            if i == horse_pos[0] and j == horse_pos[1]:
                board[i][j] = 1
            elif i == final_pos[0] and j == final_pos[1]:
                board[i][j] = 'x'
    return board

def horseLuis(tablero, pos, step):
    return None


inicio = list(map(int, input().strip().split()))
fin = list(map(int, input().strip().split()))
step = 1
tablero = initializeBoard(inicio, fin)
sol, esSol = horseLuis(tablero, inicio, step)
