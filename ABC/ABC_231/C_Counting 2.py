import bisect

N, Q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(Q):
    x = int(input())
    print(N - bisect.bisect_left(a, x))
