N = int(input())
a_list = [] #
b_list = [] #
c_list = [] #
for _ in range(N):
    A, B = map(int, input().split())
    a_list.append(A)
    b_list.append(B)
    c_list.append(A / B)
le = 0
sum_c = sum(c_list)
for i in range(len(c_list)):
    pre_le = le
    le += c_list[i]
    if sum_c / 2 <= le:
        ri = sum(c_list[i + 1:])
        sa = abs(ri - pre_le) * b_list[i]
        ans = (a_list[i] - sa) / 2 + sum(a_list[:i])
        if pre_le < ri:
            ans += sa
        print(ans)
        exit()
