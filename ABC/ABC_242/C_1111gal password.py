N = int(input())

ans = [1] * 11
ans[0] = ans[10] = 0

for nn in range(N - 1):
    dp = [0] * 11
    for i in range(1, 10):
        dp[i] = sum(ans[i - 1:i + 2]) % 998244353
    ans = dp
print(sum(ans) % 998244353)
