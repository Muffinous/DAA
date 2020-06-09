def isFeasible(b, r, c):
    feasible = True
    i = 1
    while feasible and i <= r:
        columnFUp = b[r - i] != c
        diagonalFRUp = b[r - i] != c - i
        diagonalFLUp = b[r - i] != c + i
        feasible = columnFUp and diagonalFRUp and diagonalFLUp
        i += 1
    return feasible


def initbattle(b, row):
    n = len(b)
    if row >= n:
        is_sol = True
    else:
        is_sol = False
        col = 0
        while col < len(b) and not is_sol:
            if isFeasible(b, row, col):
                b[row] = col
                [b, is_sol] = initbattle(b, row + 1)
                if not is_sol:
                    b[row] = 0
            col += 1
    return b, is_sol


n, players = map(int, input().strip().split())
if players == 0:
    print('ADELANTE')

else:
    board = [0] * n
    rows = list(map(int, input().strip().split()))

    for i in range(players):
        board[i] = rows[i]
    [b, sol] = initbattle(board, players)
    if sol:
        print('ADELANTE')
    else:
        print('VUELVE A EMPEZAR')