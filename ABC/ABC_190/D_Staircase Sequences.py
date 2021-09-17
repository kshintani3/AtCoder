n = int(input())
k = 0
ans = 0
nn = int(n ** 0.5)

for i in range(1, nn):
    k += i
    if n < k:
        break
    if (n - k) % i == 0:
        ans += 2

print(ans)
