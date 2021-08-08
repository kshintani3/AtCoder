import sys

sys.setrecursionlimit(300000)

N = int(input())

c = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    c[a - 1].append(b - 1)
    c[b - 1].append(a - 1)

ans = []
for i in range(N):
    c[i].sort()


def dfs(x, y):
    ans.append(y + 1)
    for nxt in c[y]:
        if nxt != x:
            dfs(y, nxt)
            ans.append(y + 1)
    return


dfs(-1, 0)
print(*ans)
