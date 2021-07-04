n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = k // n
a_dict = {}

for i in range(n):
    a_dict[a[i]] = ans

k = k % n

b = sorted(a)

for i in range(k):
    a_dict[b[i]] += 1

for i in range(n):
    print(a_dict[a[i]])
