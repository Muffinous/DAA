from collections import deque


def mediasuperiorOigual(playerPoints, media):
    while playerPoints:
        points = playerPoints.popleft()

        if points >= media:
            print(points)


playerPoints = deque()
numberPlayers = int(input())
count = 0

for i in range(numberPlayers):
    x = int(input().strip())
    count += x
    playerPoints.append(x)

media = count / numberPlayers

#print(playerPoints)
#print(count)

mediasuperiorOigual(playerPoints, media)
