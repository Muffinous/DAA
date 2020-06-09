
def isFeasible(louvre, nextx, nexty, end):
    if 0 <= nextx < len(louvre) and 0 <= nexty < len(louvre[0]):
        if louvre[nextx][nexty] == 'P' or [nextx, nexty] == end:
            return True
        else:
            return louvre[nextx][nexty] != 'W' and louvre[nextx][nexty] != 1 and louvre[nextx][nexty] == 0


def is_solution(pos, final, points):
    return pos[0] == final[0] and pos[1] == final[1] and points == 0


def best(sol1, sol2):
    if sol1 < sol2:
        best = sol1  # se puede poner tanto el copy como así
    else:
        best = sol2
    return best


def visit(louvre, initpos, x_mov, y_mov, end, points, bestsol, k):
    if is_solution(initpos, end, points):
        bestsol = best(bestsol, k)
        print_louvre(louvre)
    else:
        i = 0
        while i < len(x_mov) and initpos != end:
            next_pos = [initpos[0] + x_mov[i], initpos[1] + y_mov[i]]
            if isFeasible(louvre, next_pos[0], next_pos[1], end):
                if louvre[next_pos[0]][next_pos[1]] == 'P':
                    points -= 1
                else:
                    louvre[next_pos[0]][next_pos[1]] = k
                [louvre, bestsol] = visit(louvre, next_pos, x_mov, y_mov, end, points, bestsol,  k + 1)
                if louvre[next_pos[0]][next_pos[1]] != 'P':
                    louvre[next_pos[0]][next_pos[1]] = 0
                    louvre[end[0]][end[1]] = 3
                else:
                    points += 1
            i += 1
    return louvre, bestsol


def print_louvre(l):
    print('Posible recorrido :')
    for i in range(n):
        for j in range(m):
            print(l[i][j], end=" ")
        print()

    print('--------------------')


n = int(input().strip())
m = int(input().strip())
louvre = []
for i in range(n):
    rows = str(input().strip())
    museum = [int(x) for x in rows.split(" ")]
    louvre.append(museum)

# right, left, down, up
x_mov = [0, 0, 1, -1]
y_mov = [1, -1, 0, 0]

points = 0
start = [0, 0]
end = [0, 0]
startx = starty = endx = endy = 0

for i in range(n):
    for j in range(m):
        if louvre[i][j] == 1:
            start[0] = i
            start[1] = j
        elif louvre[i][j] == 2:
            points += 1
            louvre[i][j] = 'P'
        elif louvre[i][j] == 3:
            end[0] = i
            end[1] = j
        elif louvre[i][j] == 4:
            louvre[i][j] = 'W'

bestsol = float('inf')

[l, best] = visit(louvre, start, x_mov, y_mov, end, points, bestsol, 1)
print(points, best)

