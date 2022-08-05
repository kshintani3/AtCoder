N = int(input())
a = [input() for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if a[i][j] == 'W' and a[j][i] == 'L':
            continue
        elif a[i][j] == 'L' and a[j][i] == 'W':
            continue
        elif a[i][j] == 'D' and a[j][i] == 'D':
            continue
        else:
            print('incorrect')
            exit()
print('correct')
