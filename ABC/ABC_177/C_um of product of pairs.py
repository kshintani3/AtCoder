N = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = 0
mod = 10 ** 9 + 7

for i in a:
    sum_a -= i
    ans += i * sum_a
print(ans % mod)
