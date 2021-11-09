N = int(input())
d = list(map(int, input().split()))
ans = 0
for x in range(N - 1):
    for y in range(x + 1, N):
        ans += d[x] * d[y]
print(ans)
