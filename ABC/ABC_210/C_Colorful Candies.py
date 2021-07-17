from collections import Counter

n, k = map(int, input().split())
c = list(map(int, input().split()))

c_list = Counter(c[:k])
ans = len(c_list)
for i in range(n - k):
    c_list[c[i]] -= 1
    c_list[c[i + k]] += 1
    if c_list[c[i]] == 0:
        c_list.pop(c[i])
    ans = max(ans, len(c_list))

print(ans)
