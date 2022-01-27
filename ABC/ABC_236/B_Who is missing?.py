import collections

N = int(input())
a = list(map(int, input().split()))
a_cn = collections.Counter(a)

for i in range(1, 1 + N):
    if a_cn[i] == 3:
        print(i)
        exit()
