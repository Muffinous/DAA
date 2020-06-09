import time


def imprimir(dibujo):
    for i in range(len(dibujo)):
        for j in range(len(dibujo)):
            print(dibujo[i][j], end="")
        print("")


def esFactible(dibujo, etapaX, etapaY, cuadradosNegrosEnFila, cuadradosNegrosEnColumna, intento):
    if intento == 1:
        if etapaX > 0:
            if (dibujo[etapaX - 1][etapaY] == '#') and cuadradosNegrosEnColumna[etapaY] != 0:
                return False
        if etapaY > 0:
            if (dibujo[etapaX][etapaY - 1] == '#') and cuadradosNegrosEnFila[etapaX] != 0:
                return False
        cuadradosQueNosQuedanParaDecidirSobreEllosEnFila = len(dibujo[0]) - etapaY - 1
        if cuadradosNegrosEnFila[etapaX] > cuadradosQueNosQuedanParaDecidirSobreEllosEnFila:
            return False
        cuadradosQueNosQuedanParaDecidirSobreEllosEnColumna = len(dibujo) - etapaX - 1
        if cuadradosNegrosEnColumna[etapaY] > cuadradosQueNosQuedanParaDecidirSobreEllosEnColumna:
            return False
    else:
        if (cuadradosNegrosEnFila[etapaX] == 0) or (cuadradosNegrosEnColumna[etapaY] == 0):
            return False
    return True


def BT(dibujo, etapaX, etapaY, cuadradosNegrosEnFila, cuadradosNegrosEnColumna):
    exito = False
    intento = 1
    while intento <= 2 and not exito:
        if esFactible(dibujo, etapaX, etapaY, cuadradosNegrosEnFila, cuadradosNegrosEnColumna, intento):
            if intento == 1:
                dibujo[etapaX][etapaY] = '-'
            else:
                dibujo[etapaX][etapaY] = '#'
                cuadradosNegrosEnFila[etapaX] = cuadradosNegrosEnFila[etapaX] - 1
                cuadradosNegrosEnColumna[etapaY] = cuadradosNegrosEnColumna[etapaY] - 1

            if (etapaX == len(dibujo) - 1) and (etapaY == len(dibujo[0]) - 1):
                exito = True
            else:
                if etapaY == len(dibujo[0]) - 1:
                    nuevaX = etapaX + 1
                    nuevaY = 0
                else:
                    nuevaX = etapaX
                    nuevaY = etapaY + 1
                exito = BT(dibujo, nuevaX, nuevaY, cuadradosNegrosEnFila, cuadradosNegrosEnColumna)
            if not exito:
                dibujo[etapaX][etapaY] = '-'
                if intento == 2:
                    cuadradosNegrosEnFila[etapaX] = cuadradosNegrosEnFila[etapaX] + 1
                    cuadradosNegrosEnColumna[etapaY] = cuadradosNegrosEnColumna[etapaY] + 1
        intento = intento + 1
    return exito


linea = input("")
trozos = linea.split(" ")
filas = int(trozos[0])
columnas = int(trozos[1])

dibujo = []
for i in range(filas):
    fila = ['-'] * columnas
    dibujo.append(fila)

linea = input("")
trozos = linea.split(" ")
cuadradosNegrosEnFila = []
for trozo in trozos:
    cuadradosNegrosEnFila.append(int(trozo))

linea = input("")
trozos = linea.split(" ")
cuadradosNegrosEnColumna = []
for trozo in trozos:
    cuadradosNegrosEnColumna.append(int(trozo))

start_time = time.time()

exito = BT(dibujo, 0, 0, cuadradosNegrosEnFila, cuadradosNegrosEnColumna)
if exito:
    imprimir(dibujo)
else:
    print("IMPOSIBLE")

print("--- %s seconds ---" % (time.time() - start_time))
