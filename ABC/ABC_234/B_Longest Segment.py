N = int(input())
x, y = [], []
ans = 0

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

for i in range(N - 1):
    for j in range(i + 1, N):
        li = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        if ans < li:
            ans = li
print(ans ** (1 / 2))
