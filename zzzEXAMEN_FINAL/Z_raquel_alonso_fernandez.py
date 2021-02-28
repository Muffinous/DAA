def __umbrales__(ncama, low, high, costes):
    if low > high:
        return -1

    mid = (low + high) // 2
    if costes[mid][0] == ncama:
        return mid
    elif costes[mid - 1][0] < ncama < costes[mid][0]:  # veo si esta en medio
        return mid
    elif ncama < costes[mid][0]:
        return __umbrales__(ncama, low, mid - 1, costes)
    else:
        return __umbrales__(ncama, mid + 1, high, costes)


def calc_umbrales(costes, camas):
    for i in range(len(camas)):
        ciudad = __umbrales__(camas[i], 0, len(costes) - 1, costes)
        print(costes[ciudad][1])

costes = []
ncamas = []

comunidades, umbrales = map(int, input().strip().split())

for i in range(comunidades):
    coste, comunidad = map(str, input().strip().split())
    costes.append((int(coste), comunidad))
costes.sort()

for i in range(umbrales):
    umbral = int(input().strip())
    ncamas.append(umbral)

calc_umbrales(costes, ncamas)
