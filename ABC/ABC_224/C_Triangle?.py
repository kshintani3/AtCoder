import itertools

N = int(input())

xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
xy_ind = [i for i in range(N)]
ans = 0
for i1, i2, i3 in itertools.combinations(xy_ind, 3):
    x1, y1 = x[i1], y[i1]
    x2, y2 = x[i2], y[i2]
    x3, y3 = x[i3], y[i3]
    if x1 == x2 == x3 or y1 == y2 == y3:
        continue
    elif y1 != y2 and x1 != x2 and y3 != y2 and x3 != x2 and (y1 - y2) / (x1 - x2) == (y3 - y2) / (x3 - x2):
        continue
    ans += 1
print(ans)
