def imprimirSolucion(matriz):
    N = len(matriz)
    M = len(matriz[0])
    for fil in range(N):
        for col in range(M):
            if matriz[fil][col] == float('inf'):
                print('#', end=' ')
            else:
                print(matriz[fil][col], end=' ')

        print()


def esFactible(lab, fila, columna):
    return fila >= 0 and fila < len(lab) and columna >= 0 and columna < len(lab[0]) and (
                lab[fila][columna] >= 3 or lab[fila][columna] == 1)


def allVisited(visited):
    return all(visited)


def salirDelLaberinto(lab, f, c, finF, finC, paso, seccion, visited):
    if f == finF and c == finC and allVisited(lab):
        esSol = True
    else:
        esSol = False
        mov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i = 0
        while not esSol and i < len(mov):
            sigF = mov[i][0]
            sigC = mov[i][1]
            nuevaF = f + sigF
            nuevaC = c + sigC
            if esFactible(lab, nuevaF, nuevaC):
                secc = lab[nuevaF][nuevaC]
                lab[nuevaF][nuevaC] = paso
                if not visited[secc]:
                    visited[secc] = True
                [lab, esSol] = salirDelLaberinto(lab, nuevaF, nuevaC, finF, finC, paso - 1, seccion, visited)
                if not esSol:
                    lab[nuevaF][nuevaC] = secc
            i += 1
    return [lab, esSol]


def findPos(lab, demanded, nf, nc):
    x = None
    y = None
    for i in range(nf):
        for j in range(nc):
            element = lab[i][j]
            if element == demanded:
                x = i
                y = j
    return x, y


'''
6 7 4
2 2 2 2 2 2 2
2 2 1 2 2 0 2
2 6 6 2 3 3 2 
2 6 6 2 3 3 2
2 2 5 5 4 2 2 
2 2 2 2 4 2 2 
---------------------
10

'''
lab = []
nf, nc, ns = map(int, input().strip().split())
for i in range(nf):
    fila = list(map(int, input().strip().split()))
    lab.append(fila)

seccion = set()
visited = []
for i in range(3):
    visited.append(True)
for i in range(3, ns + 3):
    seccion.add(i)
    visited.append(False)

Xini, Yini = findPos(lab, 0, nf, nc)  # porque el 0 indica start
Xfin, Yfin = findPos(lab, 1, nf, nc)  # porque el 1 indica destination

paso = -1
lab[Xini][Yini] = paso

[lab, esSol] = salirDelLaberinto(lab, Xini, Yini, Xfin, Yfin, paso - 1, seccion, visited)

'''imprimirSolucion(lab)'''
print(-lab[Xfin][Yfin])
