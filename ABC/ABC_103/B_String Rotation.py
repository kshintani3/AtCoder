S = input()
T = input()
S_len = len(S)

for i in range(S_len):
    if S == T[i:] + T[:i]:
        print("Yes")
        exit()
print("No")
