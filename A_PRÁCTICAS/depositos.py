import timeit
# THIS IS THE GOOD ONE


def calculate_vol(data, mid):
    vol = 0
    for i in range(data['depossits']):
        if data['height'][i] > mid:
            vol += data['area'][i] * mid
        else:
            vol += data['area'][i]*data['height'][i]
    return vol


def solve(data, low, top):
    mid = (low + top) // 2
    vol = calculate_vol(data, mid)
    if data['v'] == vol:
        print(mid)
        return mid
    elif data['v'] < vol:
        solve(data, low, mid - 1)
    else:
        solve(data, mid + 1, top)


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
    area, height = map(int, input().strip().split())
    data['area'].append(area)
    data['height'].append(height)

# start = timeit.default_timer()
solve(data, 0, max(data['height']))
# stop = timeit.default_timer()
# print('Time: ', stop - start)
