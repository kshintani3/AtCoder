n = int(input())
a = list(map(int, input().split()))

ans = 0

a_list = [0] * 200

for i in range(n):
    a_list[a[i] % 200] += 1

for i in range(200):
    x = a_list[i]
    ans += x * (x - 1) / 2

print(int(ans))
