N = int(input())
p = list(map(int, input().split()))
p_min = 1000000
ans = 0
for i in p:
    if p_min >= i:
        ans += 1
        p_min = i
print(ans)
