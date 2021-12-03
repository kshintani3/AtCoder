A, B, X, Y = map(int, input().split())
ab = min(abs(A - B), abs(A - B - 1))

print(min(ab * Y + X, (ab * 2 + 1) * X))
