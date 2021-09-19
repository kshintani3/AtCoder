import math

R, X, Y = map(int, input().split())

k = math.sqrt(X ** 2 + Y ** 2)
i = 0

ans = 0
if k < R:
    ans = 1
while k > i:
    ans += 1
    i += R

print(ans)
