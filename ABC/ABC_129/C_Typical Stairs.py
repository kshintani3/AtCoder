N, M = map(int, input().split())
s = [0] * (N + 2)
s[1], mod = 1, 1000000007

for _ in range(M):
    s[int(input()) + 1] = -1

for i in range(2, N + 2):
    if s[i] >= 0:
        s[i] = (max(s[i - 1], 0) + max(s[i - 2], 0)) % mod
print(s[-1])
