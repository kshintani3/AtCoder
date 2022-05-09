_ = int(input())
T = input()
dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]

dir_n = 0
ans_x = 0
ans_y = 0

for i, si in enumerate(T):
    if si == 'S':
        ans_x += dir[dir_n][0]
        ans_y += dir[dir_n][1]
    else:
        dir_n = (dir_n + 1) % 4
print(ans_x, ans_y)
