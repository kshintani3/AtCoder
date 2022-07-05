N = input()
nl = len(N) - 1
ans = 0
d = 998244353

for i in range(nl):
    cn = 10 ** (i + 1) - 10 ** i
    ans += (1 + cn) * cn // 2
    ans %= d

n_cn = int(N) - 10 ** nl + 1
ans += (1 + n_cn) * n_cn // 2

print(ans % d)
