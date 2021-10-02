N = int(input())
cn_dict = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a in cn_dict.keys():
        cn_dict[a] += 1
    else:
        cn_dict[a] = 1
    if a + b in cn_dict.keys():
        cn_dict[a + b] -= 1
    else:
        cn_dict[a + b] = -1
cn_sorted = sorted(cn_dict.keys())

ans_list = [0] * (N + 1)
cnt = 0
pre_i = 0
for i in cn_sorted:
    ans_list[cnt] += i - pre_i
    cnt += cn_dict[i]
    pre_i = i

print(*ans_list[1:N + 1])
