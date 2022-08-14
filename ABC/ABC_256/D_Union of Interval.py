import heapq

N = int(input())
q, ans = [], []
heapq.heapify(q)

for _ in range(N):
    l, r = map(int, input().split())
    heapq.heappush(q, [l, r])

s, e = 0, 0
for i in range(len(q)):
    l, r = heapq.heappop(q)
    if e < l:
        ans.append([s, e])
        s = l
        e = r
    elif l <= e < r:
        e = r
ans.append([s, e])

for i in ans[1:]:
    print(*i)
