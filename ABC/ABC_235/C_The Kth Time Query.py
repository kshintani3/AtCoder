N, Q = map(int, input().split())
a = list(map(int, input().split()))
a_max = max(a)
a_dict = {}

for i in a:
    a_dict[i] = [0]

for i in range(N):
    a_dict[a[i]].append(i + 1)

for _ in range(Q):
    x, k = map(int, input().split())
    if a_dict.get(x) is None or len(a_dict[x]) <= k:
        print(-1)
    else:
        print(a_dict[x][k])
