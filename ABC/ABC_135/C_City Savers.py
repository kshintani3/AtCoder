N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sum(a)

for i in range(N):
    if a[i] >= b[i]:
        a[i] -= b[i]
    else:
        b_can = b[i] - a[i]
        a[i] = 0
        a[i + 1] = max(0, a[i + 1] - b_can)
print(ans - sum(a))
