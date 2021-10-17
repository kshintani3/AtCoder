import collections

N = int(input())
a = list(map(int, input().split()))
a_cnt = collections.Counter(a)
for i in range(N):
    print(a_cnt[i + 1])
