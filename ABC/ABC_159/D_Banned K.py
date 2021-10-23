import collections

N = int(input())
a = list(map(int, input().split()))
a_cnt = collections.Counter(a)
a_comb = 0
for i in a_cnt.values():
    a_comb += i * (i - 1) // 2

for i in a:
    print(a_comb - a_cnt[i] + 1)
