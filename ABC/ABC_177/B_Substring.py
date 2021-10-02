S = input()
T = input()
S_len = len(S)
T_len = len(T)
ans = 0

for i in range(S_len - T_len + 1):
    cn = 0
    for j in range(T_len):
        if S[i + j] == T[j]:
            cn += 1
    if cn > ans:
        ans = cn
print(T_len - ans)
