import itertools

N = int(input())
a = list(map(int, input().split()))
b = list(itertools.accumulate(a))
x = 0
a_max = 0

for i in range(N):
    x += b[i]
    a_max = max(a_max, a[i])
    print(x + a_max * (i + 1))
