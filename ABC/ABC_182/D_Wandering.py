_ = int(input())
a = list(map(float, input().split()))

x, x_pre, ans, ma = 0, 0, 0, 0

for i in a:
    x += i
    ma = max(x, ma)
    ans = max(ans, x_pre + ma)
    x_pre += x

print(int(ans))
