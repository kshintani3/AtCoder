N, M = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]

b00 = b[0][0]
b00_7 = (b00 - 1) // 7
for j in range(1, M):
    if (b[0][j] - 1) // 7 != b00_7:
        print("No")
        exit()
for i in range(N):
    for j in range(M):
        if b[i][j] - b00 != i * 7 + j:
            print("No")
            exit()
print("Yes")
