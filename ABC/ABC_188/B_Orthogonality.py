N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * N

for i in range(N):
    c[i] = a[i] * b[i]

if sum(c) == 0:
    print("Yes")
else:
    print("No")
