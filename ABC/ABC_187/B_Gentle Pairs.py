N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
            ans += 1
print(ans)
