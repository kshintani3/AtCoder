N = int(input())
a = [0] + list(map(int, input().split()))
b, c = 0, 0

for i in range(1, N + 1):
    if i == a[i]:
        b += 1
    elif i == a[a[i]]:
        c += 1

print(c // 2 + b * (b - 1) // 2)
