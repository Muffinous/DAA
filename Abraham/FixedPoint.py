def __findFindex__(start, end, elements):
    if start >= end:
        return - 1
    mid = (start + end) // 2

    if mid == elements[mid]:
        return mid
    elif elements[mid] < mid:
        return __findFindex__(mid + 1, end, elements)
    else:
        return __findFindex__(start, mid - 1, elements)

def findFixedPoint(elements):
    return __findFindex__(0, len(v), elements)

v = [-3, -2, -1, 0, 1, 5]

index = findFixedPoint(v)

print(index, v[index])