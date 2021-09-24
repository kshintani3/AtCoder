_ = int(input())
a = list(map(int, input().split()))

ans = 0
gcd = 0
gcd_max = 0

for i in range(2, 1001):
    gcd = 0
    for b in a:
        if b % i == 0:
            gcd += 1
    if gcd_max < gcd:
        ans = i
        gcd_max = gcd
print(ans)
