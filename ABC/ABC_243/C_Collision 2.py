N = int(input())
xys = []
for _ in range(N):
    xys.append(list(map(int, input().split())))
S = input()

for i in range(N):
    xys[i].append(S[i])

xys.sort(key=lambda x: (x[1], x[0]))
for i in range(N - 1):
    if xys[i][1] == xys[i + 1][1] and xys[i][2] == "R" and xys[i + 1][2] == "L":
        print("Yes")
        exit()
print("No")
