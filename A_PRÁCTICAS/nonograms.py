def print_solution(sol):
    n = len(sol)
    for row in range(n):
        for column in range(len(sol[0])):
            print(sol[row][column], end='')
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


def checkRowFeasible(sol, r, c, h_seen):
    if c > 0:
        if (sol[r][c - 1] == '-' or sol[r][c - 1] == '#') and c - 1 == 0:
            return True
        elif h_seen[len(h_seen)-1] and sol[r][c - 1] == '#':
            return True
        elif not h_seen[len(h_seen)-1] and sol[r][c - 1] == '-':
            return True
        return False
    else:
        return True


def isFeasible(sol, row_value, column_value, row, column, h_seen):
    null_values = row_value != 0 and column_value != 0  # there are still numbers

    if not null_values:
        return False
    else:
        row_feasible = checkRowFeasible(sol, row, column, h_seen)
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


def nojumps(sol, r, c, rows, columns):
    if r < len(sol) and c < len(sol[r]):
        return c + rows[r] <= len(sol[r]) and r + columns[c] <= len(sol)
    return False


def nonogram_solve(sol, rows, columns, r, c, h_seen):
    if allEmpty(rows, columns):
        is_sol = True
    else:
        is_sol = False
        while not is_sol and nojumps(sol, r, c, rows, columns) and rows[r] > 0 and max(columns[c:len(columns)]) <= len(rows) - r:
            # c + rows[r] <= len(sol[r]) is to make sure I can fill the row if the first # is in the column c
            if isFeasible(sol, rows[r], columns[c], r, c, h_seen):
                sol[r][c] = '#'
                h_seen.append(True)
                rows[r] -= 1
                columns[c] -= 1
                [sol, is_sol] = nonogram_solve(sol, rows, columns, r, c + 1, h_seen)  # next column
                if not is_sol:
                    sol[r][c] = '-'
                    rows[r] += 1
                    columns[c] += 1
                    h_seen.pop()
            c += 1
        if r < len(sol):
            if isFullRow(rows[r]) and r < len(sol):
                [sol, is_sol] = nonogram_solve(sol, rows, columns, r + 1, 0, [False])  # next row
    return sol, is_sol


def initializeNonogram(rows, columns):
    grid = [['-'] * columns for i in range(rows)]  # initialize the nonogram values to 0
    return grid


nrows, ncolumns = map(int, input().strip().split())

r_numbers = str(input().strip())
rows = [int(x) for x in r_numbers.split(" ")]

c_numbers = str(input().strip())
columns = [int(x) for x in c_numbers.split(" ")]

solution = initializeNonogram(nrows, ncolumns)

h_seen = [False]
row = 0
column = 0
[solution, success] = nonogram_solve(solution, rows, columns, row, column, h_seen)
if success:
    print_solution(solution)
else:
    print('IMPOSIBLE')

