N = int(input())
h = list(map(int, input().split()))
m = 0
hi = 0
ans = 0
for i in h:
    if hi >= i:
        m += 1
    else:
        if m > ans:
            ans = m
        m = 0
    hi = i
print(max(ans, m))
