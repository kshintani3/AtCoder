N, L = map(int, input().split())
a = [i for i in range(L, L + N)]
a_s = sum(a)
if L >= 0:
    print(a_s - a[0])
else:
    print(a_s if N + L > 0 else a_s - a[-1])
