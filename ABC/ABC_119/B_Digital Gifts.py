N = int(input())
ans = 0.0
for _ in range(N):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        x = x * 380000
    ans += x
print(ans)
