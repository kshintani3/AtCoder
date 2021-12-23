N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    if i >= K:
        ans += 1
    else:
        for j in range(1, 18):
            if i * (2 ** j) >= K:
                break
        ans += 1 / (2 ** j)
print(ans / N)
