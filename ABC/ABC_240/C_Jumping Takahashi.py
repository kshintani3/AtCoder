N, X = map(int, input().split())
dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    ai, bi = map(int, input().split())
    for j in range(X + 1):
        if dp[i][j]:
            if j + ai <= X:
                dp[i + 1][j + ai] = True
            if j + bi <= X:
                dp[i + 1][j + bi] = True
print("Yes" if dp[-1][X] else "No")
