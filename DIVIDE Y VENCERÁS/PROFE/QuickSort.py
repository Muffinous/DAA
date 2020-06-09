from random import randint


def quicksort(elements):
    __quicksort__(0, len(elements) - 1, elements)


def __quicksort__(start, end, elements):
    if start >= end:  # empty list or partition
        return

    # divide: we use a pivot
    pivot = __partition__(elements, end, start)
    # conquer: recursively sort each partition
    __quicksort__(start, pivot - 1, elements)  # elements <= pivot
    __quicksort__(pivot + 1, end, elements)  # elements > pivot
    # No combination is required since since the
    # ordering is done "in place"


def __partition__(elements, end, start):
    # we arbitrarily use the first element as pivot
    # to use another element, we only have to swap it
    # with the first element
    pivot = elements[start]

    # we swap elements from left and right
    # elements to the left <= pivot < elements to the right
    left = start + 1
    right = end
    while left <= right:
        if elements[left] <= pivot:
            left += 1
        elif elements[right] > pivot:
            right -= 1
        else:
            elements[left], elements[right] = elements[right], elements[left]
            left += 1
            right -= 1

    # After the while-loop the following post-conditions are true:
    # · right is the index of the last element in the left partition
    # · right is a valid index in the array.
    # · right may point to the pivot itself if there are no
    # elements in the left partition
    # · left is equal to right+1
    # · left could ALSO be equal to end+1 if the right partition is empty
    # (if there are no elements greater than the pivot) and it could be
    # an invalid index outside the array.

    # we move the pivot to element[mid] to exclude it from the recursive calls
    elements[start], elements[right] = elements[right], elements[start]
    return right


def test_quicksort():
    print("Testing... ", end="")
    for i in range(10000):
        input = []
        n = randint(1, 1000)
        for j in range(n):
            input.append(randint(1, 100))
        copy = input[:]
        quicksort(input)
        copy.sort()
        assert copy == input
    print("Done.")


print("Introduce varios numeros en la misma linea separados por espacios")
numbers = [int(x) for x in input().split()]
quicksort(numbers)
print(numbers)
#test_quicksort()
