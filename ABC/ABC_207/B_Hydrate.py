from math import ceil

a, b, c, d = map(int, input().split())
aa = c * d - b

if aa <= 0:
    print(-1)
else:
    ans = ceil(a / aa)
    print(ans)
