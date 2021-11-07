import itertools

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

xy_list = [[0] * N for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        xy_list[i][j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
        xy_list[j][i] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
t = 0
total = 0
for i in itertools.permutations(range(N)):
    t += 1
    for j in range(len(i) - 1):
        total += xy_list[i[j]][i[j + 1]]
print(total / t)
