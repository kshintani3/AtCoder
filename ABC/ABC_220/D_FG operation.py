import copy

N = int(input())
a = list(map(int, input().split()))

b_list = [0] * 10
b_list[a[0]] = 1

for i in range(1, N):
    a_list = [0] * 10
    for j in range(10):
        if b_list[j] > 0:
            a_list[(a[i] + j) % 10] += b_list[j] % 998244353
            a_list[(a[i] * j) % 10] += b_list[j] % 998244353
    b_list = copy.copy(a_list)

for i in b_list:
    print(i % 998244353)
