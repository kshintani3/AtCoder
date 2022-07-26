from math import gcd


def wa(x):
    return (1 + x) * x // 2


N, A, B = map(int, input().split())
lcm = (A * B) // gcd(A, B)
print(wa(N) - A * wa(N // A) - B * wa(N // B) + lcm * wa(N //lcm))
