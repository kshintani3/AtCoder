X = input()
N = int(input())
ans_list = {}

for _ in range(N):
    S = input()
    S_len = len(S)
    cnt = 0
    for i in range(S_len):
        cnt += X.index(S[i]) + 26 * (S_len - i - 1)
    ans_list[cnt] = S

S_cnt = sorted(ans_list.keys(), reverse=True)
print(ans_list)
for i in S_cnt:
    print(ans_list[i])
