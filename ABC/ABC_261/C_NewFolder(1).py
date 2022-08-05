from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    s = input()
    d[s] += 1
    if d[s] > 1:
        print(s + '(' + str(d[s] - 1) + ')')
    else:
        print(s)
