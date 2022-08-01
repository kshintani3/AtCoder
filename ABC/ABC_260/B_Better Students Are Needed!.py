a, b, c, d = map(int, input().split())
ili = [a - i for i in range(a)]

x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = []

xi = zip(x, ili)
xi = sorted(xi, reverse=True)

for i in range(b):
    ii = a - xi[i][1]
    ans.append(ii)
    x[ii] = -1
    y[ii] = -1

yi = zip(y, ili)
yi = sorted(yi, reverse=True)

for i in range(c):
    ii = a - yi[i][1]
    ans.append(ii)
    x[ii] = -1
    y[ii] = -1

z = [x[j] + y[j] for j in range(a)]
zi = zip(z, ili)
zi = sorted(zi, reverse=True)

for i in range(d):
    ii = a - zi[i][1]
    ans.append(ii)

for an in sorted(ans):
    print(an + 1)
