T = int(input())
for _ in range(T):
    ans = 0
    L, R = map(int, input().split())
    if R < 2 * L:
        print(0)
    else:
        r2 = R - L * 2 + 1
        ans = (1 + r2) * r2 / 2
        print(int(ans))
