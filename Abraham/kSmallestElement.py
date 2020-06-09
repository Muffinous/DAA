#k es una posicion, da todos los que son mayores y menores que el
def kthSmallestElement(k, elements):
    mid = len(elements) // 2
    pivot = elements[mid]

def median(elements):
    ordinal = (len(elements) + 1) // 2
    return kthSmallestElement(ordinal -1, elements)

def test():
    print("Testing... ", end="")

v = [1, 3, 5, 2, 6, 4, 7] #no hace falta ordenarlo, es lo que evitamos, la mediana seria el 4.
#v = [-3, -2, -1, 0, 1, 5]
median(v)