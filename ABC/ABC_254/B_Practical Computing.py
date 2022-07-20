N = int(input())

ans = [0, 1, 0]
for i in range(N):
    print(*ans[1:-1])
    ans = [0] + [ans[j] + ans[j + 1] for j in range(i + 2)] + [0]
