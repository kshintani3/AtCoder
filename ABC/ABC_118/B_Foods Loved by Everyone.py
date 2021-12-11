N, M = map(int, input().split())
li = set(range(1, M + 1))
for _ in range(N):
    ka = list(map(int, input().split()))
    a = set(ka[1:])
    li = li & a
print(len(li))
