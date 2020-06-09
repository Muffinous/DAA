def print_sol(sol):
    for i in range(0, len(sol)):
        if i < len(sol)-1:
            print(sol[i][0], sol[i][1], end=" ")
        else:
            print(sol[i][0], sol[i][1], end="")


def merge(left, right):
    i = j = 0
    h1 = h2 = 0
    sol = []
    corner = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            h1 = left[i][1]
            corner = left[i][0]
            i += 1
        elif left[i][0] > right[j][0]:
            h2 = right[j][1]
            corner = right[j][0]
            j += 1
        else:
            h1 = left[i][1]
            h2 = right[j][1]
            corner = left[i][0]
            j += 1
            i += 1
        max_height = max(h1, h2)
        if not sol or max_height != sol[-1][1]:
            sol.append((corner, max_height))

    # Append the remaining strips in skyline1 to the result
    while i < len(left):
        sol.append(left[i])
        i += 1

    # Append the remaining strips in skyline2 to the result
    while j < len(right):
        sol.append(right[j])
        j += 1

    return sol


def skyline(buildings):
    if len(buildings) < 2:
        return [[buildings[0][0], buildings[0][1]], [buildings[0][2], 0]]

    mid = len(buildings) // 2

    left = skyline(buildings[:mid])
    right = skyline(buildings[mid:])

    return merge(left, right)


nbuildings = int(input().strip())

buildings = []


for i in range(nbuildings):
    start, height, end = map(int, input().strip().split())
    buildings.append((start, height, end))

# print(' my data ', buildings)

sol = skyline(buildings)
print_sol(sol)
