def printsol(levels, playerlvl, pos, nlvl):
    if pos < 0:  # not founded
        if levels[0] > playerlvl:
            print("X", levels[0])
        elif levels[nlvl - 1] < playerlvl:
            print(levels[nlvl - 1], "X")
        else:
            pos = -pos - 1
            print(levels[pos - 1], levels[pos])
    else:  # founded
        if levels[0] > playerlvl:
            print("X", levels[0])
        elif levels[nlvl - 1] < playerlvl:
            print(levels[nlvl - 1], "X")
        elif levels[nlvl - 1] == playerlvl:
            print(levels[pos - 1], "X")
        elif levels[0] == playerlvl:
            print("X", levels[pos + 1])
        else:
            print(levels[pos - 1], levels[pos + 1])


def __inLevels__(playerlvl, low, high, levels):
    if low > high:
        return -low - 1  # false
    mid = (low + high) // 2
    if levels[mid] == playerlvl:
        return mid
    elif levels[mid] > playerlvl:
        return __inLevels__(playerlvl, low, mid - 1, levels)
    else:
        return __inLevels__(playerlvl, mid + 1, high, levels)


def bs_levels(levels, players_lvls, nLevels):
    for playerlvl in players_lvls:
        pos = __inLevels__(playerlvl, 0, len(levels) - 1, levels)
        printsol(levels, playerlvl, pos, nLevels)


nLevels = int(input().strip())
levels = list(map(int, input().split()))
nPlayers = int(input().strip())
players = list(map(int, input().split()))

bs_levels(levels, players, nLevels)

