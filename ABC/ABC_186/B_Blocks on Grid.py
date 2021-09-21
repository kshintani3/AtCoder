H, W = map(int, input().split())

a = []
a_min = 100

for i in range(H):
    array = list(map(int, input().strip().split()))
    a.append(array)
    if min(array) < a_min:
        a_min = min(array)

ans = 0
for i in range(H):
    for j in range(W):
        ans += a[i][j] - a_min
print(ans)
