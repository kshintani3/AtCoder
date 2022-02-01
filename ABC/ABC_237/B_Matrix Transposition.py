H, W = map(int, input().split())
a = []

for i in range(H):
    ai = list(input().split())
    a.append(ai)

for i in range(W):
    for j in range(H):
        print(a[j][i], end=" ")
    print()
