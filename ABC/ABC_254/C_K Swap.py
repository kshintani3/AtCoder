N, K = map(int, input().split())
a = [0] * (K - N % K) + list(map(int, input().split()))

x, y = K, len(a) // K
b = [[0] * y for _ in range(x)]
for j in range(y):
    for i in range(x):
        b[i][j] = a[i + j * x]

c = []
for i in b:
    c.append(sorted(i))

pre = 0
for j in range(y):
    for i in range(x):
        if pre > c[i][j]:
            print('No')
            exit()
        pre = c[i][j]
print('Yes')
