H, W = map(int, input().split())
ans = []
for i in range(H):
    for j, sj in enumerate(input()):
        if sj == 'o':
            ans.append(i)
            ans.append(j)

print(abs(ans[0] - ans[2]) + abs(ans[1] - ans[3]))
