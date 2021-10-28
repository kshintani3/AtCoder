import collections

N = int(input())
s = sorted(input() for _ in range(N))
s_list = collections.Counter(s)

s_max = max(s_list.values())
for i in s_list.keys():
    if s_list[i] == s_max:
        print(i)
