import collections

N = int(input())
a = list(map(int, input().split()))
a_sum = sum(a)
a_cnt = collections.Counter(a)
Q = int(input())

for _ in range(Q):
    B, C = map(int, input().split())
    a_sum += (C - B) * a_cnt[B]
    a_cnt[B], a_cnt[C] = 0, a_cnt[B] + a_cnt[C]
    print(a_sum)
