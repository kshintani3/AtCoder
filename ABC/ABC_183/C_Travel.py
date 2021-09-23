import itertools

N, K = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for v in itertools.permutations(range(1, N)):
    t_sum = 0
    s = 0
    for i in v:
        t_sum += t[s][i]
        s = i
    t_sum += t[s][0]
    if t_sum == K:
        ans += 1
print(ans)
