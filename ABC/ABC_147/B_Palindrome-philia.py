S = input()
s_len = len(S) // 2
ans = 0
for i in range(s_len):
    if S[i] != S[-i - 1]:
        ans += 1
print(ans)
