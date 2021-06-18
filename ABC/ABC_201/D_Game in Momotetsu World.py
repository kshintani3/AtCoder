h, w = map(int, input().split())
s = [list(input()) for l in range(h)]

taka = 0.0
ao = 0.0
for i in range(h):
    for m in range(w):
        a = s[i][m]
        if i == 0 & m == 0:
            continue
        elif a == '+':
            if (i + m) % 2 == 1:
                taka += 1.0
            else:
                ao += 1.0
        elif a == '-':
            if (i + m) % 2 == 1:
                taka -= 1.0
            else:
                ao -= 1.0

if taka > ao:
    print("Takahashi")
elif taka == ao:
    print("Draw")
else:
    print("Aoki")
