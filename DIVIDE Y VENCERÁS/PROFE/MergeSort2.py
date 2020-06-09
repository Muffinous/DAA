from random import randint, shuffle


def mergesort(elements):
    if len(elements) < 2:
        return

    mid = len(elements) // 2
    # divide
    left = elements[:mid]
    right = elements[mid:]

    # conquer
    mergesort(left)
    mergesort(right)

    # combine
    merge(left, right, elements)


def merge(first, second, output):
    # we append two auxiliary values
    # that will act as limiters
    first.append(float('inf'))
    second.append(float('inf'))

    k = f = s = 0
    while f < len(first) - 1 or s < len(second) - 1:
        if first[f] <= second[s] and f < len(first) - 1:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1


def test_mergesort():
    print("Testing... ", end="")
    for i in range(10000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1, 100))
        shuffle(input)
        copy = input[:]
        mergesort(input)
        copy.sort()
        assert copy == input
    print("Done")


# print("Introduce varios numeros en la misma linea separados por espacios")
# numbers = [int(x) for x in input().split()]
# mergesort(numbers)
# print(numbers)
test_mergesort()
