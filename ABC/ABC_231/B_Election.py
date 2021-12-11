n = int(input())
s = []
for _ in range(n):
    s.append(input())
cn = []
s_li = []
for i in set(s):
    s_li.append(i)
    cn.append(s.count(i))
print(s_li[cn.index(max(cn))])
