S = input()
ans = 753
for i in range(len(S) - 2):
    ans = min(ans, abs(int(S[i:i + 3]) - 753))
print(ans)
