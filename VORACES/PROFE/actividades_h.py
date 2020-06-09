def esFactible(ultimaActividad, actividad):
    return ultimaActividad <= actividad[0]


def Actividades(actividades):
    nActividades = 0
    ultimaActividad = 0 # Indica la hora de fin de la última actividad seleccionada
    for j in range(len(actividades)):
        # Si la fecha de inicio es igual o superior a la actividad elegida anteriormente
        if esFactible(ultimaActividad, actividades[j]):
            nActividades += 1
            ultimaActividad = actividades[j][1]
    return nActividades


T = int(input())
for i in range(T):
    N = int(input())    # numero de actividades programadas
    lista = list(map(int, input().strip().split()))[:2*N]
    actividades = [[0, 0] for _ in range(N)]
    j = 0
    for i in range(N):
        actividades[i][0] = lista[j]
        actividades[i][1] = lista[j+1]
        j += 2
    actividades.sort(key=lambda x: (x[1]))
    A = Actividades(actividades)   # numero maximo de actividades
    print()
    print(A, end="")
