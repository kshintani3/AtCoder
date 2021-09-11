import array
from bisect import bisect_left

L, Q = map(int, input().split())

cut_list = array.array("i", [0, L])

for _ in range(Q):
    c, x = map(int, input().split())
    b = bisect_left(cut_list, x)
    if c == 1:
        cut_list.insert(b, x)
    else:
        print(cut_list[b] - cut_list[b - 1])
