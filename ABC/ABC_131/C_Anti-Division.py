def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


A, B, C, D = map(int, input().split())
CD = lcm(C, D)
c_cn = B // C - A // C + (A % C == 0)
d_cn = B // D - A // D + (A % D == 0)
cd_cn = B // CD - A // CD + (A % CD == 0)
print(B - A + 1 - c_cn - d_cn + cd_cn)
