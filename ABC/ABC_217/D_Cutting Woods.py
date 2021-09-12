import array
from bisect import bisect_left, insort

L, Q = map(int, input().split())

cut_list = array.array("i", [0, L])

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        insort(cut_list, x)
    else:
        b = bisect_left(cut_list, x)
        print(cut_list[b] - cut_list[b - 1])
