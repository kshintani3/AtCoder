from bisect import bisect

_, _, N = map(int, input().split())

xy = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*xy)]

a_so = sorted(set(a))
b_so = sorted(set(b))

for i in range(N):
    ans_a = bisect(a_so, a[i])
    ans_b = bisect(b_so, b[i])
    print(ans_a, ans_b)
