from collections import Counter
from itertools import product

N, K = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0

for tf in product((True, False), repeat=N):
    ss = ''
    for i, flag in enumerate(tf):
        if flag:
            ss += S[i]
    c = [i for i in Counter(ss).values()]
    ans = max(c.count(K), ans)

print(ans)
