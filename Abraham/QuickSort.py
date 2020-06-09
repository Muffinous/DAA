from random import randint, shuffle


def __partition__(elements, start, end):
    pivot = elements[start]
    left = start + 1
    right = end
    while left <= right:
        if elements[left] <= pivot:
            left += 1
        elif elements[left] > pivot:
            right -= 1
        else:
            elements[left], elements[right] = elements[right], elements[left]
            left += 1
            right -= 1

        elements[start], elements[right] = elements[right], elements[start]
    return start

def quicksort(elements):
    __qs_rec__(0, len(elements) - 1, elements)


def __qs_rec__(start, end, elements):
    if start >= end:
        return
    pivot = __partition__(elements, start, end)
    __qs_rec__(start, pivot - 1, elements)
    __qs_rec__(pivot + 1, end, elements)

def test_quicksort():
    print("Testing ....", end="")
    for i in range(1000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1, 100))
        shuffle(input)  # desordena aleatoriamente
        copy = input[:]  # copia literal del array, si fuese input[] apunta a lo mismo
        quicksort(input)
        copy.sort()
        assert copy == input
    print("Done")

test_quicksort()