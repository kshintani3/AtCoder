n, k = map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
ni, ki = [list(i) for i in zip(*xy)]

pl = k
d = zip(ni, ki)
d = sorted(d)
ni, ki = zip(*d)

for i in range(n):
    if pl >= ni[i]:
        pl += ki[i]
    else:
        break

print(pl)
