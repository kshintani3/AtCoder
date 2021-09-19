from itertools import product

N = int(input())
A = list(map(int, input().split()))

mi = 2 ** 30

for bit in product((True, False), repeat=N - 1):
    bit = list(bit) + [True]
    a_or = 0
    a_xor = 0
    for i in range(N):
        a_or = a_or | A[i]
        if bit[i]:
            a_xor = a_xor ^ a_or
            a_or = 0
    if a_xor < mi:
        mi = a_xor
print(mi)
