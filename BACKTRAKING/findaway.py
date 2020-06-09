def isFeasible(l, next_x, next_y):
    return 0 <= next_x < len(l) and 0 <= next_y < len(l) and l[next_x][next_y] == 0 and not next_y == next_x == 0


def are0anywhere(lab):
    for i in range(len(lab)):
        for j in range(len(lab)):
            if lab[i][j] == 0 and not i == j == 0:
                return False
    return True


def isSolution(lab, start_x, start_y):
    full = are0anywhere(lab)
    return start_x == len(lab) - 1 and start_y == len(lab) - 1 and full


def solve(lab, start_x, start_y, x_mov, y_mov, k):
    max = len(x_mov)
    if isSolution(lab, start_x, start_y):
        is_sol = True
    else:
        is_sol = False
        i = 0
        while not is_sol and i < max and lab[len(lab)-1][len(lab)-1] == 0:
            if isFeasible(lab, start_x + x_mov[i], start_y + y_mov[i]):
                lab[start_x + x_mov[i]][start_y + y_mov[i]] = k
                [lab, is_sol] = solve(lab, start_x + x_mov[i], start_y + y_mov[i], x_mov, y_mov, k + 1)
                if not is_sol:
                    lab[start_x + x_mov[i]][start_y + y_mov[i]] = 0
            i += 1
    return lab, is_sol


def print_lab(lab):
    for i in range(len(lab)):
        print(lab[i])


n = int(input().strip())
labyrinth = []
for i in range(n):
    lab = str(input().strip())
    laby = [int(x) for x in lab.split(" ")]
    labyrinth.append(laby)

# right, left, down, up
x_mov = [0, 0, 1, -1]
y_mov = [1, -1, 0, 0]
step = 1

[labyrinth, exist] = solve(labyrinth, 0, 0, x_mov, y_mov, step)
if exist:
    print('SI')
else:
    print('NO')
