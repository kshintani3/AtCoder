N, Q = map(int, input().split())
pre_train = [0] * (N + 1)
back_train = [0] * (N + 1)

for _ in range(Q):
    ans = []
    a = list(map(int, input().split()))
    if len(a) == 3:
        if a[0] == 1:
            back_train[a[1]] = a[2]
            pre_train[a[2]] = a[1]
        else:
            back_train[a[1]] = 0
            pre_train[a[2]] = 0
    else:
        a1 = a[1]
        while pre_train[a1] != 0:
            a1 = pre_train[a1]
        ans.append(a1)
        while back_train[a1] != 0:
            a1 = back_train[a1]
            ans.append(a1)
        print(len(ans), *ans)
