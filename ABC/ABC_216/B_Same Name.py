N = int(input())
xy = [map(str, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

ans = "No"

for i in range(N - 1):
    for j in range(i + 1, N):
        if x[i] == x[j]:
            if y[i] == y[j]:
                ans = "Yes"
                break
print(ans)
