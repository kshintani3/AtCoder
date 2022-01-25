N = int(input())

if N < 105:
    print(0)
else:
    ans = 0
    for i in range(105, N + 1, 2):
        cn = 1
        for j in range(2, i + 1):
            if i % j == 0:
                cn += 1
            if cn > 8:
                break
        if cn == 8:
            ans += 1
    print(ans)
