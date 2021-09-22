N = int(input())
y_list = []

for i in range(N):
    s, t = input().split()
    y_list.append((s, int(t)))

d = sorted(y_list, key=lambda x: (x[1]), reverse=True)
print(d[1][0])
