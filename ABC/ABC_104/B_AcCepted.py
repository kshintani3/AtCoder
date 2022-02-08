S = input()
ans = True
cn = 0
ac = ["A", "C"]

for i in range(2, len(S) - 1):
    if S[i] == "C":
        cn += 1

for i in range(len(S)):
    if S[i] not in ac and S[i].isupper():
        ans = False

if S[0] == "A" and cn == 1 and ans:
    print("AC")
else:
    print("WA")
