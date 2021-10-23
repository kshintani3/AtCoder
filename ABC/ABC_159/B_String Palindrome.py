S = input()
N = len(S)
S_f = S[:N // 2]
S_b = S[N // 2 + 1:]
if S != S[::-1] or S_f != S_f[::-1] or S_b != S_b[::-1]:
    print("No")
else:
    print("Yes")
