import collections

N = int(input())
s_li = []

for _ in range(N):
    s = list(input())
    s_li.append("".join(sorted(s)))

ans = 0
ans_li = collections.Counter(s_li)
for i in ans_li.values():
    ans += i * (i - 1) // 2
print(ans)
