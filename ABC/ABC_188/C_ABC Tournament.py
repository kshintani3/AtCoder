N = int(input())
a = list(map(int, input().split()))

a1 = max(a[:2 ** (N - 1)])
a2 = max(a[2 ** (N - 1):])

if a1 < a2:
    print(a.index(a1) + 1)
else:
    print(a.index(a2) + 1)
