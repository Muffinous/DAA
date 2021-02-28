def printsol(wrd, final):
    long = len(final)
    print(wrd + ";", end="")
    for i in range(0, long - 1):
        print(final[i], end="")
        print("|", end="")

    print(final[long - 1], end="")  # we need to print the last one without the |


def count(w, pipe):
    return pipe.count(w)


str = "br;hbfrbr|brnsbr|kdlbrsbrbr"
div = str.split(";")

word = div[0]
parts = div[1].split('|')
answ = []

for i in range(0, len(parts)):
    times = count(word, parts[i])
    answ.append(times)

printsol(word, answ)
