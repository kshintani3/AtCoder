from collections import deque

N, M = map(int, input().split())

edge = [[] for _ in range(N)]

INF = 1 << 60
MOD = 10 ** 9 + 7

for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

dist = [INF] * N
dp = [0] * N
dist[0] = 0
dp[0] = 1

que = deque((0,))

while que:
    u = que.popleft()
    curr_cost = dist[u]
    next_cost = curr_cost + 1

    for v in edge[u]:
        if next_cost < dist[v]:
            que.append(v)
            dist[v] = next_cost

        if next_cost == dist[v]:
            dp[v] += dp[u]
            dp[v] %= MOD

print(dp[-1])
