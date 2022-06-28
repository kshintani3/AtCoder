N = 0
ans_list = []

while True:
    a = int(input())
    if N == 0:
        N = a
        print(1, flush=True)
        ans_list.append(1)
    else:
        if a == 0:
            exit()
        else:
            ans_list.append(a)
            ans_list.sort()
            if len(ans_list) == 2 * N + 1:
                exit()
            for i in range(2, 2 * N + 2):
                if i not in ans_list:
                    print(i, flush=True)
                    ans_list.append(i)
                    break
