def summer(data, estado):
    found = False
    best = 0
    for w in range(len(data['estado'])):
        for j in range(len(data['estado'][w])):
            if data['estado'][w][j] == estado:
                found = True
                if data['gasto'][w][j] > best:
                    best = data['gasto'][w][j]
    return best + 1, found


data = {
    'weeks': 0,
    'estado': [],
    'gasto': []
}


w = int(input().strip())
data['weeks'] = w
for i in range(w):
    data['estado'].append([])
    data['gasto'].append([])
    status = int(input().strip())
    for j in range(status):
        st, g = map(str, input().strip().split())
        data['estado'][i].append(st)
        data['gasto'][i].append(int(g))
p = int(input().strip())
estados = []
for i in range(p):
    output = str(input().strip())
    estados.append(output)

for i in range(p):
    [max, found] = summer(data, estados[i])
    if found:
        print(max)
    else:
        print('?')
