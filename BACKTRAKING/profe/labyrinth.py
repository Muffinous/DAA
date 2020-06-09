import numpy as np


def initializeLabyrinth():
    labyrinth = np.zeros([10, 10])
    walls = np.array([[0, 2], [0, 7], [1, 0], [1, 2], [1, 5], [1, 6], [1, 8], [2, 6], [2, 8], [3, 1], [3, 4], [3, 5],
                      [3, 6], [4, 2], [4, 3], [4, 7], [5, 5], [5, 7], [6, 0], [6, 3], [6, 4], [6, 7], [6, 9], [7, 1],
                      [7, 2], [7, 8], [7, 9], [8, 2], [8, 4], [8, 5]])
    labyrinth[walls[:, 0], walls[:, 1]] = np.inf  # initialize the walls with inf
    return labyrinth


def isSolution(labyrinth, r, c):
    return r == np.size(labyrinth, 0) - 1 and c == np.size(labyrinth, 1) - 1


def isFeasible(lab, f, c):
    return 0 <= f < np.size(lab, 0) and 0 <= c < np.size(lab, 1) and lab[f][c] == 0


def escapeLabyrinth(labyrinth, r, c, k):
    if isSolution(labyrinth, r, c):
        isSol = True
    else:
        isSol = False
        mov = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
        i = 0
        while not isSol and i < np.size(mov, 0):
            if isFeasible(labyrinth, r + mov[i, 0], c + mov[i, 1]):
                labyrinth[r + mov[i, 0], c + mov[i, 1]] = k
                [labyrinth, isSol] = escapeLabyrinth(labyrinth, r + mov[i, 0], c + mov[i, 1], k + 1)
                if not isSol:
                    labyrinth[r + mov[i, 0], c + mov[i, 1]] = 0
            i += 1
    return labyrinth, isSol


lab = initializeLabyrinth()
xIni = 0
yIni = 0
step = 1
lab[xIni, yIni] = step  # I print myself!!

[lab, isSol] = escapeLabyrinth(lab, xIni, yIni, step)
print(lab)
