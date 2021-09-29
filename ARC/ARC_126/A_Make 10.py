T = int(input())
ten_comb = [(0, 1, 1), (2, 1, 0), (1, 0, 2), (3, 0, 1), (5, 0, 0)]

for _ in range(T):
    ans = 0
    N2, N3, N4 = map(int, input().split())
    N3 //= 2
    for a, b, c in ten_comb:
        k = max(N2, N3, N4)

        if a > 0:
            k = min(k, N2 // a)
        if b > 0:
            k = min(k, N3 // b)
        if c > 0:
            k = min(k, N4 // c)

        ans += k
        N2 -= a * k
        N3 -= b * k
        N4 -= c * k

    print(ans)
