n = int(input())
a = list(map(int, input().split()))
b = 10 ** 9 + 7

a.sort()

ans = a[0]
ans += 1

for i in range(n-1):
    if a[i] == a[i+1]:
        continue
    ans *= (a[i+1] - a[i] + 1)
    
print(ans%b)
