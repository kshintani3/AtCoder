import itertools

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

for i, j, m in itertools.combinations(range(N), 3):
    if x[i] == x[j] or x[i] == x[m]:
        if x[j] == x[m]:
            print("Yes")
            exit()
    elif (y[j] - y[i]) / (x[j] - x[i]) == (y[m] - y[i]) / (x[m] - x[i]):
        print("Yes")
        exit()
print("No")
