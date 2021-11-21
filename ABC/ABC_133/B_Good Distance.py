N, D = map(int, input().split())
x = []
ans = 0

for _ in range(N):
    x.append(list(map(int, input().split())))

for i in range(N - 1):
    y = x[i]
    for j in range(i + 1, N):
        z = x[j]
        tol = 0
        for l in range(D):
            tol += (y[l] - z[l]) ** 2
        if tol ** 0.5 % 1 == 0:
            ans += 1
print(ans)
