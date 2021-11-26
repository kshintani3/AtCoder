N = int(input())
s, p = [], []
ni = list(range(1, N + 1))
for i in range(N):
    si, pi = input().split()
    s.append(si)
    p.append(int(pi))
table = zip(ni, s, p)
ans = sorted(table, key=lambda x: (x[1], -(x[2])))
for i, _, _ in ans:
    print(i)
