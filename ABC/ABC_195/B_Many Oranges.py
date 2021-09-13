import math

a, b, k = map(int, input().split())
k *= 1000

mi = int(math.ceil(k / b))
ma = int(math.floor(k / a))

if mi <= ma:
    print(mi, ma)
else:
    print("UNSATISFIABLE")
