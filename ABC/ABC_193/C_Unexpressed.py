import math

N = int(input())

n_list = []

a_max = math.ceil(math.sqrt(N))
b_max = math.ceil(N / 2)

for a in range(2, a_max + 1):
    for b in range(2, b_max + 1):
        if a ** b > N:
            break
        n_list.append(a ** b)
n_len = len(set(n_list))
print(N - n_len)
