def DyV(edificios):
    if not edificios: return []
    if len(edificios) == 1:
        return [[edificios[0][0], edificios[0][1]], [edificios[0][2], 0]]  # Ej: [[1, 11], [5, 0]]
    mid = len(edificios) // 2
    left = DyV(edificios[:mid])
    right = DyV(edificios[mid:])
    return merge(left, right)


def merge(left, right):
    h1, h2, res = 0, 0, []
    while left and right:
        if left[0][0] < right[0][0]:
            pos, h1 = left[0]
            left = left[1:]
        elif left[0][0] > right[0][0]:
            pos, h2 = right[0]
            right = right[1:]
        else:
            pos, h1 = left[0]
            h2 = right[0][1]
            left = left[1:]
            right = right[1:]
        H = max(h1, h2)
        if not res or H != res[-1][1]:
            res.append([pos, H])
    if left:
        res += left
    if right:
        res += right
    return res


C = int(input())
edificios = [0] * C
for i in range(0, C):
    x = input().strip().split()
    ei = int(x[0])
    h = int(x[1])
    ef = int(x[2])
    edificios[i] = [ei, h, ef]

result = DyV(edificios)
final = len(result)
for i in range(0, final):
    if i < final-1:
        print(result[i][0], result[i][1], end=" ")
    else:
        print(result[i][0], result[i][1], end="")
