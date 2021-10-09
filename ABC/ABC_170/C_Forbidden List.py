from bisect import bisect

X, N = map(int, input().split())
if N == 0:
    print(X)
else:
    p = list(map(int, input().split()))
    not_p = [i for i in range(102) if i not in p]
    ind = bisect(not_p, X)
    print(not_p[ind] if not_p[ind] - X < X - not_p[ind - 1] else not_p[ind - 1])
