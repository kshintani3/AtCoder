N, K, A = map(int, input().split())
for i in range(K - 1):
    A = (A + 1) % N
print(A if A != 0 else N)
