N = int(input())

ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += (b + a) / 2 * (b - a + 1)
print(int(ans))
