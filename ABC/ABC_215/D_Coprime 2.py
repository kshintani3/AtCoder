N, M = map(int, input().split())
A = list(map(int, input().split()))

L = 10 ** 5 + 1
x = [False] * L

for i in A:
    x[i] = True

div = []
for i in range(2, L):
    for j in range(i, L, i):
        if x[j]:
            div.append(i)
            break

ok_list = [True] * (M + 1)
for d in div:
    for j in range(d, M + 1, d):
        ok_list[j] = False

cnt = sum(ok_list) - 1
print(cnt)

for i in range(1, M + 1):
    if ok_list[i]:
        print(i)
