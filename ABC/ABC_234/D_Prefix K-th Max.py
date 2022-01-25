from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
p = list(map(int, input().split()))
pq = p[:K]
heapify(pq)
print(pq)
print(pq[0])

for x in p[K:]:
    heappush(pq, x)
    heappop(pq)
    print(pq[0])
