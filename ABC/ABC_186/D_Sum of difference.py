N = int(input())
a = list(map(int, input().split()))

a_list = [0] * N

a.sort()
ans = 0
s = 0
for i in range(N):
    ans += i * a[i] - s
    s += a[i]

print(ans)
