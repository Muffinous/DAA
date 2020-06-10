# INPUT
# 6 7 4
# 2 2 2 2 2 2 2
# 2 2 1 2 2 0 2
# 2 6 6 2 3 3 2
# 2 6 6 5 3 3 2
# 2 2 5 5 4 2 2
# 2 2 2 2 4 2 2


def searchIn(ikea, n, m):
    for i in range(n):
        for j in range(m):
            if ikea[i][j] == 0:
                return i, j

def isFeasible(ikea, newR, newC):
    if ikea[newR][newC] == 2:
        return False
    else:
        return True

def isSolution(labyrinth, r, c, visited, rooms):
    return labyrinth[r][c] == 1 and visited == rooms + 1

def changeRoom(old, new):
    return old != new and old != 0

def escapeLabyrinth(labyrinth, r, c, k, visited, rooms):
    if isSolution(labyrinth, r, c, visited, rooms):
        isSol = True
        print(k)
    else:
        isSol = False
        mov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i = 0
        while not isSol and i < 4:
            oldNumber = labyrinth[r][c]
            if isFeasible(labyrinth, r + mov[i][0], c + mov[i][1]):
                if changeRoom(oldNumber, labyrinth[r + mov[i][0]][c + mov[i][1]]):
                    visited += 1
                [labyrinth, isSol] = escapeLabyrinth(labyrinth, r + mov[i][0], c + mov[i][1], k + 1, visited, rooms)
                if not isSol:
                    if changeRoom(oldNumber, labyrinth[r + mov[i][0]][c + mov[i][1]]):
                        visited -= 1
            i += 1
    return labyrinth, isSol

n, m, s = map(int, input().strip().split())
ikea = []
for i in range(n):
    ikea.append([])
    ikea[i] = list(map(int, input().strip().split()))
x, y = searchIn(ikea, n, m)
print(escapeLabyrinth(ikea, x, y, 1, 0, s))
