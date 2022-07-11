N, A, B = map(int, input().split())
w, b = '', ''

for i in range(N):
    if i % 2 == 0:
        w += '.' * B
        b += '#' * B
    else:
        b += '.' * B
        w += '#' * B

for i in range(N * A):
    flag = i % (A * 2)
    if flag < A:
        print(w)
    else:
        print(b)
