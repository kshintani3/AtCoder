n, k = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, 10 ** 18
while r - l > 1:
    m = (l + r) // 2
    s = 0
    for x in a:
        s += min(x, m)
    if s >= k * m:
        l = m
    else:
        r = m
print(l)