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


def mergesort(array):
    if len(array) < 2:
        return
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    mergesort(left)
    mergesort(right)

    fusion(left, right, array)


n = int(input().strip())
# numbers = str(input().strip())

# for i in range(n):
 # arr = [int(x) for x in numbers.split(" ")]

arr = list(map(int, input().split()))
mergesort(arr)
print(' '.join(map(str, arr)))
