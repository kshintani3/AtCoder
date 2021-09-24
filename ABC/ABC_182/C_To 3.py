import itertools

N = input()
n = [int(i) for i in N]
len_n = len(n)

for i in range(len_n):
    for j in itertools.combinations(n, len_n - i):
        if sum(j) % 3 == 0:
            print(i)
            exit()
print(-1)
