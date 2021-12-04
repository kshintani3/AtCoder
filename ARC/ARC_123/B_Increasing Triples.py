N = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ai, bi, ci = 0, 0, 0
ans = 0

while True:
    if a[ai] < b[bi] < c[ci]:
        ai += 1
        bi += 1
        ci += 1
        ans += 1
    elif a[ai] >= b[bi]:
        bi += 1
    elif b[bi] >= c[ci]:
        ci += 1
    if max(ai, bi, ci) >= N:
        break
print(ans)
