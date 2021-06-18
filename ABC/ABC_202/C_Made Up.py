n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = [0] * (n + 1)
for i in range(n):
    cnt[b[c[i] - 1]] += 1

ans = 0
for s in range(n):
    ans += cnt[a[s]]

print(ans)
