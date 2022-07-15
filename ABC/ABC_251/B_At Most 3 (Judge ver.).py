import itertools

_, W = map(int, input().split())
a = list(map(int, input().split())) + [0, 0]
ans = [False] * (W + 1)

for j in itertools.combinations(a, 3):
    if sum(j) <= W:
        ans[sum(j)] = True

print(sum(ans))
