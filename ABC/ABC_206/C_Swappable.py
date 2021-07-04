from sys import setrecursionlimit
import collections

setrecursionlimit(10 ** 6)

N = int(input())
a = list(map(int, input().split()))
a.sort()
a_len = len(a)
ans = 0

c = collections.Counter(a)

a = list(set(a))

a_count = []
a_sum = []

for i in a:
    a_count.append(c[i])

for i in range(len(a)-1):
    ans += a_count[i] * (a_len - a_count[i])
    a_len -= a_count[i]

print(ans)
