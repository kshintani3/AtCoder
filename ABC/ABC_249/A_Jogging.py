a, b, c, d, e, f, x = map(int, input().split())

ax, ay = divmod(x, a + c)
dx, dy = divmod(x, d + f)
ans = (ax * a + min(ay, a)) * b - (dx * d + min(dy, d)) * e

if ans < 0:
    print('Aoki')
elif ans == 0:
    print('Draw')
else:
    print('Takahashi')
