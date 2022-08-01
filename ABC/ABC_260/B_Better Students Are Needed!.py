N, X, Y, Z = map(int, input().split())
ind = list(range(N))
ind.reverse()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

xi = sorted(zip(a, ind))
for i in range(X):
    ii = N - xi[-i - 1][1]
    ans.append(ii)
    a[ii - 1], b[ii - 1] = -1, -1

yi = sorted(zip(b, ind))
for i in range(Y):
    ii = N - yi[-i - 1][1]
    ans.append(ii)
    a[ii - 1], b[ii - 1] = -1, -1

z = [a[j] + b[j] for j in range(N)]
zi = sorted(zip(z, ind))
for i in range(Z):
    ii = N - zi[-i - 1][1]
    ans.append(ii)

for i in sorted(ans):
    print(i)
