N, Q = map(int, input().split())

a = list(range(N + 1))
b = list(range(N + 1))

for _ in range(Q):
    x = int(input())
    i = a[x]
    if i == N:
        y = b[i - 1]
    else:
        y = b[i + 1]
    j = a[y]

    a[x], a[y] = j, i
    b[i], b[j] = y, x

print(*b[1:])
