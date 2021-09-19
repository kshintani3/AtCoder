N = int(input())
a = list(map(int, input().split()))

ans = 0
a_list = [0] * 200

for i in a:
    a_list[i % 200] += 1

for x in a_list:
    ans += x * (x - 1) // 2

print(ans)
