N, K = map(int, input().split())
a = list(map(int, input().split()))
x, y = [], []
l, n = [], []

for i in range(1, N + 1):
    xy = list(map(int, input().split()))
    if i in a:
        l.append(xy)
    else:
        n.append(xy)

ans = 0
for ni in n:
    d = float('inf')
    for li in l:
        d = min(d, ((ni[0] - li[0]) ** 2 + (ni[1] - li[1]) ** 2) ** 0.5)
    ans = max(ans, d)
print(ans)
