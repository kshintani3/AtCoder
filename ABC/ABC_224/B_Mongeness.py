H, W = map(int, input().split())
s = [list(map(int, input().split())) for i in range(H)]

for i1 in range(H - 1):
    for i2 in range(i1 + 1, H):
        for j1 in range(W - 1):
            for j2 in range(j1 + 1, W):
                if s[i1][j1] + s[i2][j2] > s[i1][j2] + s[i2][j1]:
                    print("No")
                    exit()
print("Yes")
