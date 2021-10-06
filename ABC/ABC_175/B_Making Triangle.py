import itertools

N = int(input())
L = list(map(int, input().split()))
L_set = list(set(L))

ans = 0
for i, j, k in itertools.combinations(L_set, 3):
    if i + j + k - max(i, j, k) * 2 > 0:
        ans += L.count(i) * L.count(j) * L.count(k)

print(ans)
