import math

a, b, k = map(int, input().split())
k *= 1000

mi = math.ceil(k / b)
ma = math.floor(k / a)

if mi <= ma:
    print(mi, ma)
else:
    print("UNSATISFIABLE")
