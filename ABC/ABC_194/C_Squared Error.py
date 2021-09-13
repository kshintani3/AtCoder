a = int(input())
b = list(map(int, input().split()))

ans = 0
b_sum = sum(b)

for i in b:
    ans += (a - 1) * i ** 2 - 2 * (i * (b_sum - i))
    b_sum -= i

print(ans)
