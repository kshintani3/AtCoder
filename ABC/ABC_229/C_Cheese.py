N, W = map(int, input().split())
a, b = [], []
for _ in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ab = zip(a, b)
ab = sorted(ab, key=lambda x: x[0], reverse=True)

total = 0
ans = 0
for ai, bi in ab:
    if total + bi >= W:
        ans += (W - total) * ai
        break
    total += bi
    ans += ai * bi
print(ans)
