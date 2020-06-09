from collections import deque


def countingNames(namesChilds, namesParents):
    while namesParents:
        name = namesParents.popleft()
        count = 0

        for i in range(len(namesChilds)):
            if name == namesChilds[i]:
                count += 1
        #print(x)
        if count == 0:
            print("NUEVO")
        else:
            print(count)


namesChilds = []
namesParents = deque()

numberChilds = int(input())

for i in range(numberChilds):
    x = (input().strip())
    namesChilds.append(x)

#print(namesChilds)

numberNames = int(input())

for i in range(numberNames):
    x = (input().strip())
    namesParents.append(x)

#print(namesParents)

countingNames(namesChilds, namesParents)
