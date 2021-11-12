N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

pre_ai = -1
ans = 0

for ai in a:
    ans += b[ai - 1]
    if ai - pre_ai == 1:
        ans += c[pre_ai - 1]
    pre_ai = ai
print(ans)
