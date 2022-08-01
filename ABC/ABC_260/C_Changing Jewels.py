N, X, Y = map(int, input().split())
r, b = 1, 0

for i in range(N - 1):
    r, b = r * (1 + X) + b, (r * X + b) * Y
print(b)
