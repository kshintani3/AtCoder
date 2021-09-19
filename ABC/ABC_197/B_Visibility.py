H, W, X, Y = map(int, input().split())
s = [list(input()) for i in range(H)]

X -= 1
Y -= 1
count = 1

for l in range(Y):  # (X,Y)から左方向
    if s[X][Y - l - 1] == '.':
        count += 1
    else:
        break

for r in range(W - Y - 1):  # (X,Y)から右方向
    if s[X][Y + r + 1] == '.':
        count += 1
    else:
        break

for u in range(X):  # (X,Y)から上方向
    if s[X - u - 1][Y] == '.':
        count += 1
    else:
        break

for d in range(H - X - 1):  # (X,Y)から下方向
    if s[X + d + 1][Y] == '.':
        count += 1
    else:
        break

print(count)
