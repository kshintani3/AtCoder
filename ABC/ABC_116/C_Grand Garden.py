N = int(input())
h = list(map(int, input().split()))
pre = 0
ans = 0
for i in h:
    ans += max(i - pre, 0)
    pre = i
print(ans)
