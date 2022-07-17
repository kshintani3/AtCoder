from collections import Counter

N = int(input())
dic = {}
SS = '0123456789'
ans = 10000

for i in SS:
    dic[i] = []
for _ in range(N):
    s = input()
    for j in range(10):
        dic[s[j]].append(j)

for i in SS:
    cn = Counter(dic[i])
    if len(cn) == N:
        ans = min(ans, max(cn.keys()))
    else:
        cn_ma = max([k for k, v in cn.items() if v == max(cn.values())])
        t = cn_ma + 10 * (cn[cn_ma] - 1)
        ans = min(ans, t)
print(ans)
