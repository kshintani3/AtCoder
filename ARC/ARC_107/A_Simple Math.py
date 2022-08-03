def si(i):
    return (i * (i + 1) // 2) % mod


a, b, c = map(int, input().split())
mod = 998244353
print((si(a) * si(b) * si(c)) % mod)
