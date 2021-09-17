import itertools

n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
k = int(input())
cd = [map(int, input().split()) for _ in range(k)]

p = itertools.product(*cd)
ans = 0

for i in p:
    print(i)
    cnt = 0
    ball = set(i)
    for j in range(m):
        if a[j] in ball and b[j] in ball:
            cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)
