n = int(input())
a = list(map(int, input().split()))
flag = 0

a.sort()

for i in range(n):
    if a[i] != i + 1:
        flag = 1
        break
if flag == 0:
    print("Yes")
else:
    print("No")
