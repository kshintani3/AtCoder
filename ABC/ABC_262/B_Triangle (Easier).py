N, M = map(int, input().split())
nm = [[False] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    nm[u - 1][v - 1] = True
    nm[v - 1][u - 1] = True

ans = 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if nm[a][b] and nm[b][c] and nm[c][a]:
                ans += 1
print(ans)
