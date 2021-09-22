import math


def comb(a, b):
    return math.factorial(a) // (math.factorial(a - b) * math.factorial(b))


L = int(input())

print(int(comb(L - 1, 11)))
