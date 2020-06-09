def rec_binarysearch(e, elements):
    return __rec_bs__(e, 0, len(elements) - 1, elements)  # __ metodo privado


def __rec_bs__(e, low, high, elements):
    if low > high:
        return -low - 1  # false
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return __rec_bs__(e, low, mid - 1, elements)
    else:
        return __rec_bs__(e, mid + 1, high, elements)


v = [1, 3, 4, 5, 6, 7, 9]

index = rec_binarysearch(8, v)
print(index)