# sol = [1, 3, 0, 2] -> 0,1,2,3
# first queen is in the row 0 col 1
# second queen is in the row 1 col 3
# third queen is in the row 2 col 0
# fourth queen is in the row 3 col 2


def initializeSolution(n):
    return [0] * n  # array [0, 0, 0, 0]


def initializeBoard(n):
    row = [0] * n
    board = []
    for i in range(n):
        board.append(row[:])
    return board


def isFeasible(solution, row, column):
    feasible = True
    i = 1
    while feasible and i <= row:
        columnFeasible = solution[row - i] != column
        diagonal1Feasible = solution[row - i] != column - i
        diagonal2Feasible = solution[row - i] != column + i
        feasible = columnFeasible and diagonal1Feasible and diagonal2Feasible
        i += 1
    return feasible


def nQueensVA(solution, row):
    n = len(solution)
    if row >= n:
        isSol = True
    else:
        isSol = False
        column = 0
        while not isSol and column < n:
            if isFeasible(solution, row, column):
                solution[row] = column
                [solution, isSol] = nQueensVA(solution, row + 1)
                if not isSol:
                    solution[row] = 0
            column += 1
    return solution, isSol


def printSol(solution):
    n = len(solution)
    board = initializeBoard(n)
    for row in range(n):
        board[row][solution[row]] = 1
        for column in range(n):
            print(board[row][column], ' ', end='')
        print()


#  i don't initialize best sol cause it's a decision problem, i don't want the BEST
n = 4
row = 0
solution = initializeSolution(n)
[solution, success] = nQueensVA(solution, row)
if success:
    printSol(solution)
else:
    print('Doesnt exist')
