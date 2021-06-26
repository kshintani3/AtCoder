n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
t, l, r = [list(i) for i in zip(*xy)]

l_list = [[0] * 3 for i in range(n)]
ans = 0

for i in range(n):
    l_list[i][0], l_list[i][1], l_list[i][2] = l[i], r[i], t[i]
l_list = sorted(l_list, key=lambda x: (x[0], x[1], x[2]))

for i in range(n):
    for j in range(1, n - i):
        if l_list[i][1] > l_list[i + j][0]:
            ans += 1
        elif (l_list[i][1] == l_list[i + j][0]) and (l_list[i][2] % 2 == 1) and (l_list[i + j][2] <= 2):
            ans += 1
        elif l_list[i][1] < l_list[i + j][0]:
            break


print(ans)
