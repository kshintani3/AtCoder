def dire(x, y):
    ret = []
    for di in d:
        ss = ''
        for i in range(1, N):
            ss += a[(x + di[0] * i) % N][(y + di[1] * i) % N]
        ret.append(ss)
    return max(ret)


N = int(input())
a, b, ma = [], [], '0'
d = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

for _ in range(N):
    s = input()
    a.append(s)
    ma = max(ma, max(s))

ans = '0'
for i in range(N):
    for j in range(N):
        if a[i][j] == ma:
            ans = max(ans, dire(i, j))

print(ma + ans)
