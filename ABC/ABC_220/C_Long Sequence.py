import itertools
from bisect import bisect_right

N = int(input())
a = list(map(int, input().split()))
X = int(input())

a_sum = sum(a)
a_sum_list = list(itertools.accumulate(a))

ans = (X // a_sum) * N + bisect_right(a_sum_list, X - a_sum * (X // a_sum)) + 1

print(ans)
