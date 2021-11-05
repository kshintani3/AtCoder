import math

A, B = map(int, input().split())
C = math.gcd(A, B)
print(A * B // C)
