import collections


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N, X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x = sorted(x)
d_li = []

for i in range(N):
    d_li.append(x[i + 1] - x[i])
d_li = sorted(d_li)

d_mi = d_li[0]
c = collections.Counter(make_divisors(d_mi))
for i in sorted(c.keys(), reverse=True):
    flag = True
    for j in d_li:
        if j % i != 0:
            flag = False
            break
    if flag:
        print(i)
        break
