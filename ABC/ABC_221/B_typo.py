S = input()
T = input()
s_len = len(S)

if S == T:
    print("Yes")
else:
    cnt = []
    for i in range(s_len):
        if S[i] != T[i]:
            cnt.append(i)
    if len(cnt) == 2 and S[cnt[0]] == T[cnt[1]] and S[cnt[1]] == T[cnt[0]] and cnt[1] - cnt[0] == 1:
        print("Yes")
    else:
        print("No")
