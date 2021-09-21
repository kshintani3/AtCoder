n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*xy)]

x = - sum(a)
b_sum = 0

c = [[a[i], b[i], 2 * a[i] + b[i]] for i in range(n)]

c_sort = sorted(c, key=lambda x: x[2], reverse=True)

for j in range(n):
    x += c_sort[j][2]
    if x > 0:
        print(j + 1)
        break
