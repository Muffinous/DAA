import timeit


def calculate_vol(dep, mid):
    vol = 0
    for i in range(dep['depossits']):
        if dep['height'][i] > mid:
            vol += dep['area'][i] * mid
        else:
            vol += dep['area'][i]*dep['height'][i]
    return vol


def solve(data, top, mid):
    if top == 0:
        largest = max(data['height'])
        #print(largest)
        mid = largest // 2
    elif top <= mid:
        mid = top // 2
    else:
        mid = top
    # print('Mid ', mid)
    # print(data)
    vol = calculate_vol(data, mid)
    # print('My vol', vol)

    if data['v'] < vol:
        solve(data, mid, mid)
    elif data['v'] > vol:
        new_mid = mid + 1
        solve(data, new_mid, mid)
    elif data['v'] == vol:
        print('Level ', mid)


data = {
    'v': 0,
    'depossits': 0,
    'area': [],
    'height': [],
}
v = int(input().strip())
data['v'] = v
n = int(input().strip())
data['depossits'] = n
for i in range(n):
    area, base = map(int, input().strip().split())
    data['area'].append(area)
    data['height'].append(base)

start = timeit.default_timer()
solve(data, 0, 0)
stop = timeit.default_timer()
print('Time: ', stop - start)
