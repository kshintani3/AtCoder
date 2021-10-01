N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

ans_list = []
for i in range(N):
    ans_list.append(max(abs(x[i] - x_min), abs(x[i] - x_max), abs(y[i] - y_min), abs(y[i] - y_max)))

ans_list.sort()
print(ans_list[-3])
