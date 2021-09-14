N, K = map(int, input().split())

for _ in range(K):
    a = "".join(sorted(str(N)))
    N = int(a[::-1]) - int(a)
print(N)
