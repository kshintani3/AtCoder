def ja(ii, jj):
    x_in, y_in = [ii], [jj]
    b_x_in, b_y_in = 1, 1

    for y in range(jj + 1, H1):
        if b_y_in == H2:
            break
        if a[y][ii] == b[b_y_in][0]:
            y_in.append(y)
            b_y_in += 1

    if b_y_in != H2:
        return False

    for x in range(ii + 1, W1):
        if b_x_in == W2:
            break
        if a[jj][x] == b[0][b_x_in]:
            x_in.append(x)
            b_x_in += 1
    if b_x_in != W2:
        return False

    for i in range(1, W2):
        for j in range(1, H2):
            if a[y_in[j]][x_in[i]] != b[j][i]:
                return False
    return True


H1, W1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(H2)]
b0 = b[0][0]

for j in range(H1 - H2 + 1):
    for i in range(W1 - W2 + 1):
        if a[j][i] == b0:
            if ja(i, j):
                print('Yes')
                exit()
print('No')
