import timeit


def print_solution(sol):
    n = len(sol)
    print('My grid:', "\n")
    for row in range(n):
        for column in range(len(sol[0])):
            print(sol[row][column], ' ', end='')
        print()


def checkColumnFeasible(sol, r, c):
    count = 0
    start = 0
    end = r - 1
    first_time = 1

    for i in range(r):
        if first_time and (sol[i][c] == '#'):
            start = i
            count = count + 1
            first_time = 0

        elif sol[i][c] == '#':
            count = count + 1

    if (end - start + 1) == count or count == 0 or start == r - 1:
        return True
    else:
        return False


def checkRowFeasible(sol, r, c):
    count = 0
    start = 0
    end = c - 1
    first_time = 1

    for i in range(c):
        if first_time and (sol[r][i] == '#'):
            start = i
            count += 1
            first_time = 0

        elif sol[r][i] == '#':
            count += 1

    if (end - start + 1) == count or start == c - 1 or count == 0:
        return True
    else:
        return False


def isFeasible(sol, row_value, column_value, row, column):
    null_values = row_value != 0 and column_value != 0  # there are still numbers

    if not null_values:
        return False
    else:
        row_feasible = checkRowFeasible(sol, row, column)
        if not row_feasible:
            return False
        else:
            column_feasible = checkColumnFeasible(sol, row, column)
    return null_values and row_feasible and column_feasible


def allEmpty(row_values, column_values):
    for i in range(len(row_values)):
        if row_values[i] != 0:
            return False
    for i in range(len(column_values)):
        if column_values[i] != 0:
            return False
    return True


def isFullRow(row_value):
    return row_value == 0


def nonogram_solve(sol, rows, columns, r, c):
    if allEmpty(rows, columns):
        is_sol = True
    else:
        is_sol = False
        while not is_sol and c + rows[r] <= len(sol[r]) and r < len(sol) and c < len(sol[r]):
            # c + rows[r] <= len(sol[r]) is to make sure I can fill the row if the first # is in the column c
            if isFeasible(sol, rows[r], columns[c], r, c):
                sol[r][c] = '#'
                rows[r] -= 1
                columns[c] -= 1
                [sol, is_sol] = nonogram_solve(sol, rows, columns, r, c + 1)
                if not is_sol:
                    sol[r][c] = '-'
                    rows[r] += 1
                    columns[c] += 1
            c += 1
        if isFullRow(rows[r]):
            [sol, is_sol] = nonogram_solve(sol, rows, columns, r + 1, 0)
    return sol, is_sol


def initializeNonogram(rows, columns):
    grid = [['-'] * columns for i in range(rows)]  # initialize the nonogram values to 0
    return grid


start = timeit.default_timer()

nrows, ncolumns = map(int, input().strip().split())

r_numbers = str(input().strip())
rows = [int(x) for x in r_numbers.split(" ")]

c_numbers = str(input().strip())
columns = [int(x) for x in c_numbers.split(" ")]

solution = initializeNonogram(nrows, ncolumns)

row = 0
column = 0
[solution, success] = nonogram_solve(solution, rows, columns, row, column)
if success:
    print_solution(solution)
else:
    print('IMPOSIBLE')

stop = timeit.default_timer()
print('Time: ', stop - start)
