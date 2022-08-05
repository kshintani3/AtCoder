N, M = map(int, input().split())
x = [0] + list(map(int, input().split()))
c = [0] * (N + 1)
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    ci, yi = map(int, input().split())
    c[ci] = yi

for i in range(1, N + 1):
    for j in range(i):
        # 表の場合
        dp[i][j + 1] = dp[i - 1][j] + x[i] + c[j + 1]

        # 裏の場合
        dp[i][0] = max(dp[i][0], dp[i - 1][j])

print(max(dp[-1]))
