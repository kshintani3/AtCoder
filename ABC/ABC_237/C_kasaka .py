S = input()
S_len = len(S)
le = 0
ri = 0
for i in range(S_len):
    if S[i] != "a":
        le = i
        break
for j in range(S_len):
    if S[-j - 1] != "a":
        ri = j
        break
if le > ri:
    print("No")
    exit()
else:
    S = "a" * (ri - le) + S
    for i in range(len(S) // 2 + 1):
        if S[i] != S[-i - 1]:
            print("No")
            exit()
    print("Yes")
