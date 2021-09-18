N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(N):
    mi = a[i]
    for j in range(i, N):
        mi = min(mi, a[j])
        ans = max(ans, mi * (j - i + 1))

print(ans)
