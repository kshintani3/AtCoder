a = list(input())
# chokudai = ["c", "h", "o", "k", "u", "d", "a", "i"]
chokudai = "chokudai"
mod = 10 ** 9 + 7
n = len(a)
dp = [[0] * 9 for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(n):
    for j in range(8):
        if a[i] == chokudai[j]:
            dp[i + 1][j + 1] = (dp[i][j] + dp[i][j + 1]) % mod
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]
print(dp[n][8])
