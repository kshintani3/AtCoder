X = input()
N = int(input())
ans_list = {}

for _ in range(N):
    S = input()
    cnt = ""
    for i in S:
        cnt += chr(X.index(i) + 97)
    ans_list[cnt] = S

ans_ind = sorted(ans_list.keys())
for i in ans_ind:
    print(ans_list[i])
