H, W = map(int, input().split())
c = []
ans = 1
for _ in range(H):
    c.append(input())

w = [[True] * W for _ in range(H)]
q = [(0, 0)]
while len(q) != 0:
    x, y = q.pop()
    w[x][y] = False
    if x + 1 != H and c[x + 1][y] == "." and w[x + 1][y]:
        q.append((x + 1, y))
    if y + 1 != W and c[x][y + 1] == "." and w[x][y + 1]:
        q.append((x, y + 1))
    ans = max(ans, x + y + 1)
    if ans == W + H - 1:
        break
print(ans)
