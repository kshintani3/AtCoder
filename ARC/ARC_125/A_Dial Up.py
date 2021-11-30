N, M = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

s_sum, t_sum = sum(s), sum(t)
if (s_sum == 0 and t_sum > 0) or (s_sum == N and t_sum < M):
    print(-1)
    exit()

x = (s[0] + 1) % 2
for i in range(1, N // 2 + 1):
    if s[i] == x or s[-i] == x:
        y = i
        break

if t_sum == 0 or t_sum == M:
    print(M if s[0] == t[0] else M + y)
    exit()

ans = 0 if s[0] == t[0] else 1
for i in range(M - 1):
    if t[i] != t[i + 1]:
        ans += 1
print(ans + M + y - 1)
