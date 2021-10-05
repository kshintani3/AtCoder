N = int(input())
a = list(map(int, input().split()))
s_max = a.pop(0)
ans = 0

for i in a:
    if s_max < i:
        s_max = i
    else:
        ans += s_max - i
print(ans)
