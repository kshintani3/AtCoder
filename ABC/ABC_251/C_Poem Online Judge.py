N = int(input())
s, t = [], []
for _ in range(N):
    si, ti = input().split()
    s.append(si)
    t.append(int(ti))

d = {}
for i in range(N - 1, -1, -1):
    d[s[i]] = t[i]

ma, ans, k = 0, 0, ''
for i, j in enumerate(s):
    if k != j and ma < d[j]:
        ma, k, ans = d[j], j, i
print(ans + 1)
