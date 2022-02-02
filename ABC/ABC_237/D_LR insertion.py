N = int(input())
S = input()
L, R = [], []

for i in range(N):
    if S[i] == "R":
        L.append(i)
    else:
        R.append(i)
ans = L + [N] + R[::-1]
print(*ans)
