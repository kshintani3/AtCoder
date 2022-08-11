from bisect import bisect_left

N, Q = map(int, input().split())
s = input()
ac = []
for i in range(len(s) - 1):
    if s[i:i + 2] == 'AC':
        ac.append(i)

for _ in range(Q):
    l, r = map(int, input().split())
    print(bisect_left(ac, r - 1) - bisect_left(ac, l - 1))
