S1 = input()
S2 = input()
S3 = input()
S = [S1, S2, S3]
T = input()
ans = ""

for i in T:
    ans += S[int(i) - 1]
print(ans)
