N = int(input())
a = list(map(int, input().split()))
le = 1
ans = 0
for i in a:
    if i == le:
        le += 1
    else:
        ans += 1
print(ans if ans < N else -1)
