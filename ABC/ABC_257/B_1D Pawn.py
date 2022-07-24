N, K, Q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for j in l:
    if j == K:
        a[j - 1] = min(a[j - 1] + 1, N)
    else:
        if a[j - 1] + 1 != a[j]:
            a[j - 1] += 1
print(*a)
