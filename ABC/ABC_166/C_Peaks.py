N, M = map(int, input().split())
h = list(map(int, input().split()))
ans = [1] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] >= h[b]:
        ans[b] = 0
    if h[a] <= h[b]:
        ans[a] = 0
print(sum(ans))
