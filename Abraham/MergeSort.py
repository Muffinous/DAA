from random import randint, shuffle


def fusion(first, second, output):
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


def mergesort(elements):
    if len(elements) < 2:
        return
    mid = len(elements) // 2

    left = elements[:mid]
    right = elements[mid:]

    mergesort(left)
    mergesort(right)
    fusion(left, right, elements)


def test_mergesort():
    print("Testing ....", end="")
    for i in range(1000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1, 100))
        shuffle(input)  # desordena aleatoriamente
        copy = input[:]  # copia literal del array, si fuese input[] apunta a lo mismo
        mergesort(input)
        copy.sort()
        assert copy == input
    print("Done")


#v = [2, 3, 4, 5, 1, 8, 7, 9]

test_mergesort()
