N, K, X = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0

for i in range(N):
    y = min(a[i] // X, K)
    a[i] = a[i] - (y * X)
    K -= y
if K <= 0:
    print(sum(a) + X * abs(K))
else:
    a.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        for j in range(K):
            a[j] = 0
        print(sum(a))
