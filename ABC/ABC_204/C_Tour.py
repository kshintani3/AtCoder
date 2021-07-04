import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
pos = [[] for i in range(n)]
ans = 0

for i in range(m):
    A, B = map(int, input().split())
    pos[A - 1].append(B - 1)


def dfs(v):
    if temp[v]:
        return
    temp[v] = True
    for vv in pos[v]:
        dfs(vv)


for i in range(n):
    temp = [False] * n
    dfs(i)
    ans += sum(temp)
print(ans)
