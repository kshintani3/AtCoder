H, W = map(int, input().split())
a = []
ans = []

for _ in range(H):
    ai = input()
    if ai.count("#") != 0:
        a.append(ai)

for j in range(W):
    flag = False
    for i in range(len(a)):
        if a[i][j] == "#":
            flag = True
            break
    if flag:
        ans.append(j)

for out in a:
    for i in ans:
        print(out[i], end="")
    print()
