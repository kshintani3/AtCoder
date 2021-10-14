N, M = map(int, input().split())
a = [input() for i in range(2 * N)]

win_cnt = [0] * (2 * N)
rank = list(range(2 * N))

for i in range(M):
    for j in range(0, 2 * N - 1, 2):
        L, R = a[rank[j]][i], a[rank[j + 1]][i]
        if L + R in ["GC", "CP", "PG"]:
            win_cnt[rank[j]] += 1
        elif L + R in ["CG", "PC", "GP"]:
            win_cnt[rank[j + 1]] += 1
    rank = sorted(rank, key=lambda x: (-win_cnt[x], x))
for ans in rank:
    print(ans + 1)
