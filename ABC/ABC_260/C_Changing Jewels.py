n, x, y = map(int, input().split())
re = 1
bl = 0

for i in range(n - 1):
    re, bl = re * (1 + x) + bl, (re * x + bl) * y

print(bl)
