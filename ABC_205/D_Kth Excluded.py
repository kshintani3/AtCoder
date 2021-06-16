import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))

key = 0
count_list = []
for i in range(n):
    count_list.append(a[i] - i - 1)

for j in range(q):
    b = int(input())
    print(bisect.bisect_left(count_list, b) + b)
