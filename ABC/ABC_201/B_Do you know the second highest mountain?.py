n = int(input())
list = []
for i in range(n):
    a, b = input().split()
    list.append((a, int(b)))
d = sorted(list, key=lambda x: (x[1]), reverse=True)
print(d[1][0])
