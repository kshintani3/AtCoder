N, M = map(int, input().split())
l, r = [], []
for _ in range(M):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
ans = min(r) - max(l) + 1
print(ans if ans >= 0 else 0)
