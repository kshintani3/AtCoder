N = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for vi, ci in zip(v, c):
    if vi - ci > 0:
        ans += vi - ci
print(ans)
