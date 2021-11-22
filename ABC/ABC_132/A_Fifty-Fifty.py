S = input()
if S[0] == S[1]:
    print("Yes" if S[0] != S[2] and S[2] == S[3] else "No")
elif S[0] == S[2]:
    print("Yes" if S[0] != S[1] and S[1] == S[3] else "No")
elif S[0] == S[3]:
    print("Yes" if S[0] != S[1] and S[2] == S[1] else "No")
else:
    print("No")
