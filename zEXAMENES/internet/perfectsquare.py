def divide(start, end, sol):
    mid = int((start + end) / 2)
    if start > end:
        return -1
    elif (mid * mid) == sol:
        return int(mid)
    elif (mid * mid) > sol:
        return divide(start, mid - 1, sol)
    else:  # es menor
        return divide(mid + 1, end, sol)


number = int(input().strip())
n = divide(1, number, number)
print(n)
