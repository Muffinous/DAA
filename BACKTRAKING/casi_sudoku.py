import copy


def isFeasible(b, num, pos): # pos = [row, column]
    # Row feasible
    for i in range(len(b[0])):
        if b[pos[0]][i] == num:  # itera la column pero no la row b[row][column]
            return False
    # Column feasible
    for i in range(len(b)):
        if b[i][pos[1]] == num:  # itera la row pero no la column
            return False
    # Box feasible (?)
    box_row = pos[1] // 3
    box_col = pos[0] // 3
    for i in range(box_col*3, box_col*3 + 3):  # if box = 0,0 (first one) it would range(0,3) and (0,3)  # if box =
        # 0,1 (second one) it would range(3,6) and (0,3)
        for j in range(box_row*3, box_row*3 + 3):
            if b[i][j] == num:
                return False
    return True


def findEmpty(b):
    for i in range(len(b[0])):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return i, j
    return None


def solve(board, count, best):
    next = findEmpty(board)
    if not next:
        best = copy.deepcopy(board)
        return count + 1, best  # Sudoku finished
    else:
        if count < 2:
            for i in range(1, 10):
                if isFeasible(board, i, next):
                    board[next[0]][next[1]] = i
                    [count, best] = solve(board, count, best)
            board[next[0]][next[1]] = 0
        return count, best


def print_board(b):
    for i in range(len(b[0])):
        for j in range(len(b[0])):
            print(b[i][j], end=" ")
        print()


board = []
f = []

for i in range(9):
    f.append([])

for i in range(9):
    row = str(input().strip())
    rows = [int(x) for x in row.split(" ")]
    board.append(rows)

[n_solutions, board] = solve(board, 0, f)
if n_solutions == 1:
    print_board(board)
elif n_solutions > 1:
    print("casi sudoku")
else:
    print('imposible')
