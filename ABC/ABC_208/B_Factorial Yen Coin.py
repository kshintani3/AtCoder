import math

n = int(input())
ans = 0
n_list = [0] * 100

for i in range(100):
    kaijou = math.factorial(100 - i)
    if n < kaijou:
        continue
    elif n / kaijou > 100:
        ans += 100
        n -= kaijou * 100
    else:
        ans += n // kaijou
        n = n % kaijou

print(ans)
