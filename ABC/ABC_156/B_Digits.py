N, K = map(int, input().split())
for i in range(100):
    if N < K ** i:
        print(i)
        exit()
