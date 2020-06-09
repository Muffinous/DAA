# HERE I TRY SHIT
import timeit


def initializeBoard(horse_pos, final_pos):
    board = [[0] * 5 for x in range(5)]
    for i in range(5):
        for j in range(5):
            if i == horse_pos[0] and j == horse_pos[1]:
                board[i][j] = 1
            elif i == final_pos[0] and j == final_pos[1]:
                board[i][j] = 'x'
    return board


def isFeasible(sol, next_i, next_j):
    if 5 > next_i >= 0 and 5 > next_j >= 0:
        if sol[next_i][next_j] == 0:
            return True
        elif sol[next_i][next_j] != 0 and sol[next_i][next_j] == 'x':
            return True
    return False


def isSolution(actualpos, finalpos):
    return actualpos[0] == finalpos[0] and actualpos[1] == finalpos[1]


def best(sol1, sol2):
    if sol1 < sol2:
        best = sol1  # se puede poner tanto el copy como así
    else:
        best = sol2
    return best


def min_jumps(board, actual_i, actual_j, final_pos, x_mov, y_mov, n_jumps, best_sol):
    if isSolution((actual_i, actual_j), final_pos):
        best_sol = best(n_jumps, best_sol)  # me cojo la mejor solucion
    else:
        for i in range(8):
            next_i = actual_i + x_mov[i]
            next_j = actual_j + y_mov[i]
            if isFeasible(board, next_i, next_j):
                board[next_i][next_j] = 1
                best_sol = min_jumps(board, next_i, next_j, final_pos, x_mov, y_mov, n_jumps + 1, best_sol)
                board[next_i][next_j] = 0
                board[final_pos[0]][final_pos[1]] = 'x'
    return best_sol


start = timeit.default_timer()

posIni = str(input().strip())
horse = [int(x) for x in posIni.split(" ")]
posFin = str(input().strip())
goal = [int(x) for x in posFin.split(" ")]

board = initializeBoard(horse, goal)
x_move = [2, 1, -1, -2, -2, -1, 1, 2]
y_move = [1, 2, 2, 1, -1, -2, -2, -1]
bestSol = float('inf')
jumps = min_jumps(board, horse[0], horse[1], goal, x_move, y_move, 1, bestSol)
print(jumps)

stop = timeit.default_timer()

# print('Time: ', stop - start)
