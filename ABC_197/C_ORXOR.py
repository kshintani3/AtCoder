def kai():
    from itertools import product

    n = int(input())
    ai = list(map(int,input().split()))

    min = 2 ** 30

    for bit in product((True, False), repeat= n-1):
        bit = list(bit) + [True]
        ored = 0
        xored = 0
        for i in range(n):
            ored = ored | ai[i]
            if bit[i]:
                xored = xored ^ ored
                ored = 0
        if xored < min:
            min = xored
    print(min)

# or |
# xor ^

kai()